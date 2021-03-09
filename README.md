# NPA_Ingestion_Tool
Goal: To gather DOI's from RSS feeds and obtain the titles and abstracts for Machine Learning Classifer to determine
if the article if about Natural Products or not.

Main Script: (main.py); contains the code you want to run, calls other functions

File containing functions called in main: npa_ingestion_tool.py

rss_feed_2_doi:
    Open up file(rss_feed.txt; a single URL for RSS feed contained on each line), loop through each line in the file to get each url to parse RSS feed and Append list of DOIs to
    list for each journal. Saves a raw XML file for archive of RSS feed. Lastly, new DOI's added into SQLite3 database. Has count of how many DOI's inserted.

rss_feed_2_doi_elsevier:
    Open up file, loop through each line in the file to get each url to parse RSS feed for article title to search
    CrossRef for DOI; Append list of DOIs to list for each journal. Saves a raw XML file for archive of RSS feed.
    Lastly, added new DOI's into SQLite3 database. Has count of how many DOI's inserted.

database_query_pubmed:
    Connect to database and query DOIs for either less than/ equal to or greater than 3 weeks. If less than 3
    weeks, convert to pubmed id and search PubMed for title/abstract and updating the database if a result is found.
    If greater than equal to 3 weeks, try to parse from the RSS feed archives and also update database with any results.

database_stats_query:
    Query database for stats to return, gathers more variables to send in Slack stats message.

