import npa_ingestion_tool
from datetime import datetime
import sqlite3


def rss_feed_2_doi():
    """ Open up file, loop through each line in the file to get each url to parse RSS feed and Append list of DOIs to
    list for each journal. Saves a raw XML file for archive of RSS feed. Lastly, added new DOI's into SQLite3 database.
                        """

    with open("rss_feed.txt", "r") as my_file:
        doi_list = [npa_ingestion_tool.parse_rss(line, str(npa_ingestion_tool.no_newline(line) + "_" + datetime.now(
        ).strftime("%Y-%m-%d_%I-%M-%S_%p") + ".json")) for line in my_file]
        '''doi_list=[]
        for line in my_file:
            string = npa_ingestion_tool.get_xml(line, str(npa_ingestion_tool.no_newline(line) + "_" + datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p") + ".xml"))
            parsed_dois = npa_ingestion_tool.parse_rss(string[0])
            doi_list.append((string[1], parsed_dois))'''

    print(doi_list)

    # SQLite3 Database entry
    connection = npa_ingestion_tool.sqlite3_db_initialization("npa_database_feb_10.db")
    table_creation = npa_ingestion_tool.sqlite3_table_creation(connection)

    for journal in doi_list:
        archive_filename = journal[0]
        for doi in journal[1]:
            npa_ingestion_tool.sqlite3_insertion_only_doi(connection, doi, archive_filename)

    # Database Entry
    # Viewing; In terminal type: sqlite3 + database name
    # Then, SELECT * from DOIs;
    connection.commit()


def database_query_pubmed():
    """ Connect to database and query DOIs for either less than or equal to or greater than 3 weeks. If less than 3
    weeks, convert to pubmed id and search PubMed for title/abstract and updating the database if a result is found.
    If greater than equal to 3 weeks, try to parse from the RSS feed archives and also update database with any results.
                            """
    # Database connection and cursor object creation
    conn = npa_ingestion_tool.sqlite3_db_initialization("npa_database_feb_10.db")
    curse = conn.cursor()

    # Query PubMed (SELECT SQL statement) for DOI(title/abstract null) <3 weeks:
    new_rows = curse.execute(
        "SELECT * FROM DOIs WHERE Created > date('now', '-21 day') and Abstract IS NULL and Title is NULL")
    for doi in new_rows:
        print(doi)

    # Try to convert to pubmed ID, then try to parse title/abstract from PubMed and UPDATE the database
        pubmed_id = npa_ingestion_tool.doi_2_pmid(doi[1])  # returns type = list
        try:
            if pubmed_id:
                pubmed_id_string = ''.join(pubmed_id) # converts list (['123']) to string ('123')
                title_abstract = npa_ingestion_tool.pmid_2_abstract(pubmed_id)
                if title_abstract[1] is None or npa_ingestion_tool.blanks(title_abstract[1]) is True:
                    try:
                        conn.execute(
                            "UPDATE DOIs SET PMID = ?, Title = ?, Source = ? WHERE ID = ?",
                            (pubmed_id_string, title_abstract[0], "PubMed", doi[0]))
                    except sqlite3.Error as error:
                        print("Failed to update sqlite table", error)

                elif title_abstract[1] is not None or npa_ingestion_tool.blanks(title_abstract[1]) is False:
                    try:
                        conn.execute(
                            "UPDATE DOIs SET PMID = ?, Title = ?, Abstract = ?, Source = ? WHERE ID = ?",
                            (pubmed_id_string, title_abstract[0], title_abstract[1], "PubMed", doi[0]))
                    except sqlite3.Error as error:
                        print("Failed to update sqlite table", error)
            else:
                print("PMID error: " + str(doi[1]))
                continue
        except TypeError:
            print("TypeError")
            continue

    conn.commit() # TODO: May need to move to after second part once its complete.
    # Query PubMed (SELECT SQL statement) for DOI(title/abstract null) >= 3 weeks:
    old_rows = curse.execute(
        "SELECT * FROM DOIs WHERE Abstract IS NULL and Created <= date('now', '-21 day')")

    # Try to parse title/abstract from archived rss feed
    # Filename stored in database, use rss_parse_archive() with: file, doi with id for later
    # if len of return 2, only title; if 3 both title/abstract. If 1, nothing parsed


if __name__ == "__main__":
    rss_feed_2_doi()
    database_query_pubmed()
