# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:56:42 2021

@author: maras
"""

import feedparser
import re
import json
import sqlite3
from datetime import datetime
import os


def get_archives_rss_urls(url):
    command_string = "waybackpack --list " + str(url)
    os.system(command_string)


def parse_rss(url, preview_file):
    """ parse a RSS feed using feedparser to the gather list of DOIs from the
                specified RSS feed URL
            :param url: string of url link
            :param preview_file: json file to preview RSS parse
            :return: list of unique DOIs
            """
    # Parse RSS url w/ feedparser to get consistent format
    rss_feed = feedparser.parse(url)
    #print(rss_feed)
    # Creation of JSON file for easy viewing
    with open(preview_file, "w") as f:
        json.dump(rss_feed, f)

    # New list for found DOIs (will end up with duplicates)
    doi_list = []
    article_metadata = {}
    # Search through parsed RSS feed dictionary
    for key in rss_feed.entries:
        if key["title"]:
            print(key["title"])

        else:
            print("no find")
        for val in key.values():
            if type(val) == str:
                doi_search = re.search("(10\.\d{4,9}\/[-._;()/:A-Za-z0-9]+)", val)
                if doi_search:
                    doi_list.append(doi_search.group(1))
                    print(doi_search.group(1))
                    break

    # Remove duplicate DOIs from list
    unique_doi_list = list(set(doi_list))

    return unique_doi_list


def sqlite3_db_initialization(db_file):
    """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
    db_connection = sqlite3.connect(db_file)
    return db_connection


def sqlite3_table_creation(connection_object):
    """ create a table from the create_table_sql statement
        :param connection_object: Connection object
        :return: Cursor object or None
        """
    cursor = connection_object.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS DOIs (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Doi VARCHAR UNIQUE NOT NULL, created NOT NULL)")
    return cursor


def sqlite3_insertion(doi_input_list, cursor_object, connection_object):
    """ insert data into the SQLite3 database
            :param doi_input_list: list of DOI's
            :param cursor_object: Cursor_object
            :param connection_object: Connection object
            :return: Cursor object or None
            """
    # Data insertion into the database
    for item in doi_input_list:
        try:
            with connection_object:
                connection_object.execute("INSERT INTO DOIs(Doi, created) VALUES(?, ?)", (item, datetime.now()))
        except sqlite3.IntegrityError:
            print("Warning: Duplicate entry detected!")
            pass

    # Query database
    #for row in connection_object.execute("SELECT * from DOIs"):
        #print(row)

    #connection_object.commit()
    #connection_object.close()