import npa_ingestion_tool
from datetime import datetime


def rss_feed_2_doi():
    # Open up file, loop through each line in the file to get each url to parse RSS feed
    # Append list of DOIs to list for each journals url

    with open("rss_feed.txt", "r") as my_file:

        #list of the list of dois for each feed
        doi_list = [npa_ingestion_tool.parse_rss(line, str(npa_ingestion_tool.no_newline(line) + "_" + datetime.now(
        ).strftime("%Y-%m-%d_%I-%M-%S_%p") + ".json")) for line in my_file]
        '''doi_list=[]
        for line in my_file:
            string = npa_ingestion_tool.get_xml(line, str(npa_ingestion_tool.no_newline(line) + "_" + datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p") + ".xml"))
            parsed_dois = npa_ingestion_tool.parse_rss(string)
            doi_list.append((parsed_dois))'''
    print(doi_list)

    # SQLite3 Database entry
    connection = npa_ingestion_tool.sqlite3_db_initialization("npa_database_feb_10.db")
    cursor = npa_ingestion_tool.sqlite3_table_creation(connection)

    for journal in doi_list:
        archive_filename = journal[0]
        for doi in journal[1]:
            npa_ingestion_tool.sqlite3_insertion_only_doi(connection, doi, archive_filename)

    # Database Entry
    # Viewing; In terminal type: sqlite3 + database name
    # Then, SELECT * from DOIs;


def database_query_pubmed():
    print(1)
    # Query PubMed (SELECT SQL statement) for DOI(title/abstract null) <3 weeks:
            # Try to convert to pubmed ID, then try to parse title/abstract
    '''pubmed_id = npa_ingestion_tool.doi_2_pmid(doi)
            try:
                if pubmed_id:
                    title_abstract = npa_ingestion_tool.pmid_2_abstract(pubmed_id)
                    print(title_abstract)
                    if npa_ingestion_tool.blanks(title_abstract[1]) is False or title_abstract[1] is not None:
                        npa_ingestion_tool.sqlite3_insertion(connection, doi, title_abstract[0], title_abstract[1])
                    elif npa_ingestion_tool.blanks(title_abstract[1]) is True or title_abstract[1] is None:
                        npa_ingestion_tool.sqlite3_insertion_no_abstract(connection, doi, title_abstract[0])
                else:
                    print("PMID error: " + str(doi))
                    continue
            except TypeError:
                print("TypeError")
                continue'''
    # Query PubMed (SELECT SQL statement) for DOI(title/abstract null) >3 weeks:
            # Try to parse title/abstract from archived rss feed
                # Filename stored in database, use rss_parse_archive() with: file, doi with id for later
                # if len of return 2, only title; if 3 both title/abstract. If 1, nothing parsed


if __name__ == "__main__":
    rss_feed_2_doi()
    database_query_pubmed()