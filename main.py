import os
import npa_ingestion_tool
from datetime import datetime
import sqlite3
from dotenv import load_dotenv

load_dotenv()
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DB_PATH = os.path.join(DIR_PATH, "npa_ingestion_database.db")
WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")


def rss_feed_2_doi():
    """Open up file, loop through each line in the file to get each url to parse RSS feed and Append list of DOIs to
    list for each journal. Saves a raw XML file for archive of RSS feed. Lastly, added new DOI's into SQLite3 database.
        :return: Count of added DOIs
    """
    path_doi = os.path.join(DIR_PATH, "rss_feeds/rss_feed_with_doi.txt")
    with open(path_doi, "r") as my_file:
        """doi_list = [npa_ingestion_tool.parse_rss(line, str(npa_ingestion_tool.no_newline(line) + "_" + datetime.now(
        ).strftime("%Y-%m-%d_%I-%M-%S_%p") + ".json")) for line in my_file]
        """
        doi_list = []
        for line in my_file:
            string = npa_ingestion_tool.get_xml(
                line,
                str(
                    npa_ingestion_tool.no_newline(line)
                    + "_"
                    + datetime.now().strftime("%Y-%m-%d")
                    + ".xml"
                ),
            )
            parsed_doi_list = npa_ingestion_tool.parse_rss(string[0])
            doi_list.append((string[1], parsed_doi_list))
    print(doi_list)

    # SQLite3 Database entry
    connection = npa_ingestion_tool.sqlite3_db_initialization(DB_PATH)
    npa_ingestion_tool.sqlite3_table_creation(connection)
    doi_insert_count = 0
    for journal in doi_list:
        archive_filename = journal[0]
        for doi in journal[1]:
            doi_insert_success = npa_ingestion_tool.sqlite3_insertion_only_doi(
                connection, doi, archive_filename
            )
            if doi_insert_success:
                doi_insert_count += 1
    # Database Viewing; In terminal type: sqlite3 + database name
    # Then, SELECT * from DOIs;
    connection.commit()
    return doi_insert_count


def rss_feed_2_doi_elsevier():
    """Open up file, loop through each line in the file to get each url to parse RSS feed for article title to search
    CrossRef for DOI; Append list of DOIs to list for each journal. Saves a raw XML file for archive of RSS feed.
    Lastly, added new DOI's into SQLite3 database.
            :return: Count of added DOIs
    """
    path_no_doi = os.path.join(DIR_PATH, "rss_feeds/rss_feed_no_doi.txt")
    with open(path_no_doi, "r") as my_file:
        doi_lists = []
        for line in my_file:
            string = npa_ingestion_tool.get_xml(
                line,
                str(
                    npa_ingestion_tool.no_newline(line)
                    + "_"
                    + datetime.now().strftime("%Y-%m-%d")
                    + ".xml"
                ),
            )
            parsed_doi_list = npa_ingestion_tool.parse_rss_no_doi(string[0])
            doi_lists.append((string[1], parsed_doi_list))

    print(doi_lists)
    # SQLite3 Database entry
    connection = npa_ingestion_tool.sqlite3_db_initialization(DB_PATH)
    npa_ingestion_tool.sqlite3_table_creation(connection)
    doi_insert_count_2 = 0
    for journal in doi_lists:
        archive_filename = journal[0]
        for doi in journal[1]:
            doi_insert_success_2 = npa_ingestion_tool.sqlite3_insertion_only_doi(
                connection, doi, archive_filename
            )
            if doi_insert_success_2:
                doi_insert_count_2 += 1
    connection.commit()
    return doi_insert_count_2


def database_query_pubmed():
    """Connect to database and query DOIs for either less than or equal to or greater than 3 weeks. If less than 3
    weeks, convert to pubmed id and search PubMed for title/abstract and updating the database if a result is found.
    If greater than equal to 3 weeks, try to parse from the RSS feed archives and also update database with any results.
    """
    # Database connection and cursor object creation
    conn = npa_ingestion_tool.sqlite3_db_initialization(DB_PATH)
    curse = conn.cursor()

    # Query PubMed (SELECT SQL statement) for DOI(title/abstract null) <3 weeks:
    new_rows = curse.execute(
        "SELECT * FROM DOIs WHERE Created > date('now', '-21 day') and Abstract IS NULL and Title is NULL"
    )
    for doi in new_rows:
        print(doi)

        # Try to convert to pubmed ID, then try to parse title/abstract from PubMed and UPDATE the database
        pubmed_id = npa_ingestion_tool.doi_2_pmid(doi[1])  # returns type = list
        try:
            if pubmed_id:
                pubmed_id_string = "".join(
                    pubmed_id
                )  # converts list (['123']) to string ('123')
                title_abstract = npa_ingestion_tool.pmid_2_abstract(pubmed_id)
                if (
                    title_abstract[1] is None
                    or npa_ingestion_tool.blanks(title_abstract[1]) is True
                ):
                    try:
                        conn.execute(
                            "UPDATE DOIs SET PMID = ?, Title = ?, Source = ? WHERE ID = ?",
                            (pubmed_id_string, title_abstract[0], "PubMed", doi[0]),
                        )
                    except sqlite3.Error as error:
                        print("Failed to update sqlite table", error)

                elif (
                    title_abstract[1] is not None
                    or npa_ingestion_tool.blanks(title_abstract[1]) is False
                ):
                    try:
                        conn.execute(
                            "UPDATE DOIs SET PMID = ?, Title = ?, Abstract = ?, Source = ? WHERE ID = ?",
                            (
                                pubmed_id_string,
                                title_abstract[0],
                                title_abstract[1],
                                "PubMed",
                                doi[0],
                            ),
                        )
                    except sqlite3.Error as error:
                        print("Failed to update sqlite table", error)
            else:
                print("PMID error: " + str(doi[1]))
                continue
        except TypeError:
            print("TypeError")
            continue

    conn.commit()  # TODO: May need to move to after second part once its complete.

    # Query PubMed (SELECT SQL statement) for DOI(title/abstract null) >= 3 weeks:
    curse.execute(
        "SELECT * FROM DOIs WHERE Abstract IS NULL and Created <= date('now', '-21 day')"
    )

    # Try to parse title/abstract from archived rss feed
    # Filename stored in database, use rss_parse_archive() with: file, doi with id for later
    # if len of return 2, only title; if 3 both title/abstract. If 1, nothing parsed


def database_stats_query():
    """Query database for stats to return.
    :return: Count total DOI's, How many with titles and how many with both title/abstract
    """
    conn = npa_ingestion_tool.sqlite3_db_initialization(DB_PATH)
    curse = conn.cursor()
    total_doi_number = curse.execute("SELECT COUNT(*) FROM DOIs").fetchone()[0]
    doi_with_title = curse.execute(
        "SELECT COUNT(*) FROM DOIs WHERE Title is NOT NULL"
    ).fetchone()[0]
    doi_with_abstract_title = curse.execute(
        "SELECT COUNT(*) FROM DOIs WHERE Abstract is NOT NULL"
    ).fetchone()[0]
    return total_doi_number, doi_with_title, doi_with_abstract_title


if __name__ == "__main__":
    # DOI Insertion from Parsed RSS Feeds. Returns count of inserted DOI's
    doi_feeds_insert_count = rss_feed_2_doi()
    # DOI Insertion from Titles Parsed from RSS Feeds, Conversion to DOI via CrossRef. Returns count of inserted DOI's
    no_doi_feeds_insert_count = rss_feed_2_doi_elsevier()
    database_query_pubmed()  # Querying DOI's in DB on PubMed for title/abstract
    database_stats = (
        database_stats_query()
    )  # Querying DB for counts of rows in DB with certain columns
    total_dois = database_stats[0]
    dois_only_title = database_stats[1]
    dois_title_abstract = database_stats[2]

    # Slack Stats Messaging
    message = (
        "Inserted DOI's parsed directly from RSS feeds: {0}\nInserted DOI's via CrossRef query of RSS feed "
        "parsed title: {1}\nTotal Database DOI's: {2}\n{3} with title only \n{4} with both title and "
        "abstract.".format(
            doi_feeds_insert_count,
            no_doi_feeds_insert_count,
            total_dois,
            dois_only_title,
            dois_title_abstract,
        )
    )

    # Change to True to stop notifications from being sent
    notification_control_condition = True

    if notification_control_condition is False:
        npa_ingestion_tool.send_message(WEBHOOK_URL, message)