import npa_ingestion_tool
from datetime import datetime


def main():
    # Open up file, loop through each line in the file to get each url to parse RSS feed
    # Append list of DOIs to list for each journals url
    with open("rss_feed.txt", "r") as my_file:
        # TODO: Raw xml file archival system
        # Figure out RSS archive naming schema to log each journal name
        # Perhaps one word abbreviations for each journal and a timestamp for the filename
        doi_list = [npa_ingestion_tool.parse_rss(line, str(npa_ingestion_tool.no_newline(line) + "_" + datetime.now(
        ).strftime("%Y-%m-%d_%I-%M-%S_%p") + ".json")) for line in my_file]
        print(doi_list)

    connection = npa_ingestion_tool.sqlite3_db_initialization("npa_database2.db")
    cursor = npa_ingestion_tool.sqlite3_table_creation(connection)

    for journal in doi_list:
        for doi in journal:
            pubmed_id = npa_ingestion_tool.doi_2_pmid(doi)
            try:
                if pubmed_id:
                    title_abstract = npa_ingestion_tool.pmid_2_abstract(pubmed_id)
                    print(title_abstract)
                    if npa_ingestion_tool.blanks(title_abstract[1]) is False or title_abstract[1] is not None:
                        npa_ingestion_tool.sqlite3_insertion(connection, doi, title_abstract[0], title_abstract[1])
                    elif npa_ingestion_tool.blanks(title_abstract[1]) is True or title_abstract[1] is None:
                        npa_ingestion_tool.sqlite3_insertion_no_abstract(connection, doi, title_abstract[0])
                else:
                    print("PMID error")
                    npa_ingestion_tool.sqlite3_insertion_only_doi(connection, doi)
                    continue
            except TypeError:
                print("TypeError")
                continue

    # Database Entry
    # Viewing; In terminal type: sqlite3 + database name
    # Then, SELECT * from DOIs;


if __name__ == "__main__":
    main()
