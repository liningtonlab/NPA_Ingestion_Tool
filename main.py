import npa_ingestion_tool



def main():
    # Open up file, loop through each line in the file to get each url to parse RSS feed
    # Append list of DOIs to list for each journals url
    with open("rss_feed.txt", "r") as my_file:
        doi_list = [npa_ingestion_tool.parse_rss(line, "some_file.json") for line in my_file]
        print(doi_list)

    connection = npa_ingestion_tool.sqlite3_db_initialization("npa_database2.db")
    cursor = npa_ingestion_tool.sqlite3_table_creation(connection)

    '''for journal in doi_list:
        for doi in journal:
            pubmed_id = npa_ingestion_tool.doi_2_pmid(doi)
            try:
                if pubmed_id:
                    title_abstract = npa_ingestion_tool.pmid_2_abstract(pubmed_id)
                    print(title_abstract)
                    if npa_ingestion_tool.blanks(title_abstract[1]) is False:
                        npa_ingestion_tool.sqlite3_insertion(connection, doi, title_abstract[0], title_abstract[1])
                    elif npa_ingestion_tool.blanks(title_abstract[1]) is True:
                        npa_ingestion_tool.sqlite3_insertion_blankabs(connection, doi, title_abstract[0])
                else:
                    #TODO: Just put in the DOI
                    print("PMID error")
                    continue
            except TypeError:
                print("TypeError")
                continue'''

    # Database Entry
    # Viewing; In terminal type: sqlite3 + database name
    # Then, SELECT * from DOIs;


    # RSS Feed archives
    # get_archives_rss_urls('http://feeds.feedburner.com/acs/jnprdf')


if __name__ == "__main__":
    main()
