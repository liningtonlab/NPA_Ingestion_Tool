import npa_ingestion_tool


def main():
    # Open up file, loop through each line in the file to get each url to parse RSS feed
    # Append list of DOIs to list for each journals url
    with open("rss_feed.txt", "r") as my_file:
        doi_list = [npa_ingestion_tool.parse_rss(line, "some_file.json") for line in my_file]
        print(doi_list)

    # Database Entry
    connection = npa_ingestion_tool.sqlite3_db_initialization("NPA_Ingestion_database.db")
    cursor = npa_ingestion_tool.sqlite3_table_creation(connection)
    for journal in doi_list:
        npa_ingestion_tool.sqlite3_insertion(journal, cursor, connection)
    connection.commit()

    for row in connection.execute("SELECT * from DOIs"):
        print(row)

    # RSS Feed archives
    # get_archives_rss_urls('http://feeds.feedburner.com/acs/jnprdf')


if __name__ == "__main__":
    main()
