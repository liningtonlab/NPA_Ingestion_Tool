# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:56:42 2021

@author: maras
"""

import feedparser
import re
import json


def parse_rss(url):
    # Parse RSS url w/ feedparser to get consistent format
    rss_feed = feedparser.parse(url)

    # Creation of JSON file for easy viewing
    with open("some_file.json", "w") as f:
        json.dump(rss_feed, f)

    # New list for found DOIs (will end up with duplicates)
    doi_list = []

    # Search through parsed RSS feed dictionary
    for key in rss_feed.entries:
        for val in key.values():
            if type(val) == str:
                doi_search = re.search("(10\.\d{4,9}\/[-._;()/:A-Za-z0-9]+)", val)
                if doi_search:
                    doi_list.append(doi_search.group(1))

    # Remove duplicate DOIs from list
    unique_doi_list = list(set(doi_list))

    return unique_doi_list
