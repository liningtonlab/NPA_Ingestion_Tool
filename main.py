from npa_ingestion_tool import parse_rss, sqlite3_database

def main():
    # test = parse_rss("http://feeds.feedburner.com/acs/jnprdf")
    # test = parse_rss("https://www.thieme-connect.de/rss/thieme/en/10.1055-s-00000058.xml")
    # test = parse_rss("http://feeds.nature.com/ja/rss/current")
    # test = parse_rss("https://chemistry-europe.onlinelibrary.wiley.com/feed/10990690/most-recent")
    test = parse_rss("https://onlinelibrary.wiley.com/feed/15213773/most-recent")
    # test = parse_rss("https://www.mdpi.com/rss/journal/marinedrugs")
    # test = parse_rss("http://feeds.feedburner.com/acs/jnprdf")
    print(test)
    print(len(test))

    sqlite3_database(test)


if __name__ == "__main__":
    main()
