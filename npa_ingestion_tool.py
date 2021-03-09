# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:56:42 2021

@author: maras
"""

from datetime import datetime
from metapub import PubMedFetcher
from bs4 import BeautifulSoup
import feedparser
import re
import sqlite3
import requests
import os
from urllib.error import HTTPError
from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen, Request
import json
from Levenshtein import ratio

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def send_message(webhook_url, message):
    requests.post(webhook_url, json={"text": message})


def cross_ref_query_title(title):
    """Open up file, loop through each line in the file to get each url to parse RSS feed for article title to search
    CrossRef for DOI; Append list of DOIs to list for each journal. Saves a raw XML file for archive of RSS feed. Lastly
    , added new DOI's into SQLite3 database.
                :param: string of title
                :return: True/False for success; if success has title, DOI and similarity match. Otherwise,
                returns exception.
    """
    empty_result = {"crossref_title": "", "similarity": 0, "doi": ""}
    api_url = "https://api.crossref.org/works?"
    params = {"rows": "5", "query.bibliographic": title}
    url = api_url + urlencode(params, quote_via=quote_plus)
    print(url)
    request = Request(url)
    request.add_header(
        "User-Agent",
        "NPA Ingestion Tool (https://github.com/liningtonlab/NPA_Ingestion_Tool; mailto:andrew_maras@sfu.ca)",
    )
    try:
        ret = urlopen(request)
        content = ret.read()
        data = json.loads(content)
        items = data["message"]["items"]
        most_similar = empty_result
        for item in items:
            if "title" not in item:
                continue
            title = item["title"].pop()
            result = {
                "crossref_title": title,
                "similarity": ratio(
                    title.lower(), params["query.bibliographic"].lower()
                ),
                "doi": item["DOI"],
            }
            if most_similar["similarity"] < result["similarity"]:
                most_similar = result
        if most_similar["similarity"] < 0.75:
            return {
                "success": False,
                "result": most_similar,
                "exception": "Low Similarity",
            }
        else:
            return {"success": True, "result": most_similar}
    except HTTPError as httpe:
        return {"success": False, "result": empty_result, "exception": httpe}


def no_newline(line):
    """Takes string input and checks if blank or not
    :param line: string
    :return: returns boolean of true for a blank, false if not blank
    """
    new_line = line.rstrip("\n")
    replace_line = (
        new_line.replace("/", "")
        .replace(".", "")
        .replace(":", "")
        .replace("-", "")
        .replace("=", "")
        .replace("!", "")
        .replace("@", "")
        .replace("#", "")
        .replace("$", "")
        .replace("%", "")
        .replace("^", "")
        .replace("&", "")
        .replace("*", "")
        .replace("?", "")
    )
    return replace_line


def blanks(string):
    """Takes string input and checks if blank or not
    :param string: string
    :return: returns boolean of true for a blank, false if not blank
    """
    if string == "":
        return True
    else:
        return False


def get_xml(url, archive_filename):
    """parse a xml file retrieved with requests using feedparser to the gather list of DOIs from the
        specified xml
    :param url: url of rss feed
    :param archive_filename: The file name of the archive file
    :return: raw string of text from requests.get(url)
    """
    # Assign a user agent to avoid 403 error
    user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    # Using request to get RSS feed text from the URL using the assigned user agent as headers variable
    no_whitespace_url = url.rstrip("\n")

    path = os.path.join(DIR_PATH, "raw_xml_archive", archive_filename)

    if not os.path.exists(path):
        url_request = requests.get(no_whitespace_url, headers=user_agent)
        if not url_request.status_code == 200:
            print(f"WARNING: {url_request.status_code} for URL = {url}")
        raw_xml_str = url_request.text
        with open(path, "w", encoding="utf-8") as f:
            f.write(raw_xml_str)
        return raw_xml_str, archive_filename
    else:
        with open(path, "r", encoding="utf-8") as f:
            xml = f.read()
        return xml, archive_filename


def parse_rss(string_input):
    """parse a xml file retrieved with requests using feedparser to the gather list of DOIs from the
        specified xml
    :param string_input: raw string of text from requests.get(url)
    :return: list of unique DOIs
    """
    # Parse RSS url w/ feedparser to get consistent format
    rss_feed = feedparser.parse(string_input)

    # Creation of JSON file for easy viewing (For archive of FeedparserDict using JSON, outdated)
    """path = 'C:/Users/maras/Desktop/NPA_Ingestion_Tool/raw_xml_archive/' + archive_file
    with open(path, "x") as f:
        json.dump(rss_feed, f)"""

    # New list for found DOIs (will end up with duplicates)
    doi_list = []

    # Search through parsed RSS feed dictionary
    for key in rss_feed.entries:
        for val in key.values():
            if type(val) == str:
                doi_search = re.search("(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)", val)
                if doi_search:
                    doi_list.append(doi_search.group(1))
                    # print(doi_search.group(1))
                    break

    # Remove duplicate DOIs from list
    unique_doi_list = list(set(doi_list))

    return unique_doi_list


def parse_rss_no_doi(string_input):
    """parse a xml file retrieved with requests using feedparser to the gather list of DOIs from the
        specified xml, by searching RSS feeds for titles to query on CrossRef for DOIs.
    :param string_input: raw string of text from requests.get(url)
    :return: list of unique DOIs
    """
    # Parse RSS url w/ feedparser to get consistent format
    rss_feed = feedparser.parse(string_input)

    # Creation of JSON file for easy viewing (For archive of FeedparserDict using JSON, outdated)
    """path = 'C:/Users/maras/Desktop/NPA_Ingestion_Tool/raw_xml_archive/' + archive_file
    with open(path, "x") as f:
        json.dump(rss_feed, f)"""

    # New list for found DOIs (will end up with duplicates)
    crossref_doi_list = []

    # Search through parsed RSS feed dictionary
    for key in rss_feed.entries:
        found_title = []
        if key["title"]:
            title_1 = key["title"]
            found_title.append(title_1)
        unique_title = list(set(found_title))
        title_string = "".join(unique_title)
        crossref_query = cross_ref_query_title(title_string)
        found_doi = crossref_query["result"]["doi"]
        if crossref_query["success"]:
            crossref_doi_list.append(found_doi)
        elif not crossref_query["success"]:
            print(
                (
                    key["title"],
                    crossref_query["result"]["crossref_title"],
                    crossref_query["exception"],
                )
            )
            continue

    # Remove duplicate DOIs from list
    unique_doi_list = list(set(crossref_doi_list))

    return unique_doi_list


def doi_2_pmid(doi):
    """returns PMID for a given DOI
    :param doi:  DOI as string
    :return: PMID as string
    """
    fetch = PubMedFetcher()
    pm_id = fetch.pmids_for_query(f"{doi}[DOI]")
    return pm_id


def pmid_2_abstract(pm_id):
    """returns abstract for a given pmid
    :param pm_id: string pmid
    :return: tuple of title and abstract
    """
    fetch = PubMedFetcher()
    article = fetch.article_by_pmid(pm_id)
    article_xml = article.xml
    soup = BeautifulSoup(article_xml, "xml")
    try:
        title = soup.ArticleTitle.text
    except AttributeError:
        title = None
    try:
        abstract = soup.AbstractText.text
    except AttributeError:
        abstract = None
    return title, abstract


def sqlite3_db_initialization(db_file):
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    db_connection = sqlite3.connect(db_file)
    return db_connection


def sqlite3_table_creation(connection_object):
    """create a table from the create_table_sql statement
    :param connection_object: Connection object
    :return: Cursor object or None
    """
    cursor = connection_object.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS DOIs (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,Doi VARCHAR UNIQUE NOT NULL, PMID VARCHAR, Title VARCHAR, Abstract VARCHAR, Source VARCHAR, Filename NOT NULL, Created NOT NULL)"
    )
    return cursor


def sqlite3_insertion_only_doi(connection_object, doi, filename):
    """insert data into the SQLite3 database
    :param filename: name of archive file
    :param doi: Doi
    :param connection_object: Connection object.cursor()
    :return: None
    """
    # Data insertion into the database

    try:
        with connection_object:
            connection_object.execute(
                "INSERT INTO DOIs(Doi, PMID, Title, Abstract, Source, Filename, Created) VALUES(?, NULL, NULL, NULL, NULL, ?, ?)",
                (doi, filename, datetime.now()),
            )
            print("Successful DOI entry recorded!")
            return True
    except sqlite3.IntegrityError:
        print("Warning: Duplicate entry detected!")
        return False


# Archive parsing, not yet used
'''def sqlite3_insertion(connection_object, doi, pmid, title, abstract, source, filename):
    """ insert data into the SQLite3 database
            :param filename: name of archive file
            :param source: source of doi(Pubmed, RSS Feed, Cross ref)
            :param pmid: PubMed ID
            :param doi: Doi
            :param title: article title variable
            :param abstract: article abstract variable
            :param connection_object: Connection object.cursor()
            :return: Cursor object or None
            """
    # Data insertion into the database
    try:
        with connection_object:
            connection_object.execute("INSERT INTO DOIs(Doi, PMID, Title, Abstract, Source, Filename, Created) VALUES(?, ?, ?, NULL, NULL, ?, ?)",
                                      (doi, pmid, title, abstract, source, filename, datetime.now()))

    except sqlite3.IntegrityError:
        print("Warning: Duplicate entry detected!")
        pass


def sqlite3_insertion_no_abstract(connection_object, doi, title, filename):
    """ insert data into the SQLite3 database
            :param filename: name of archive file
            :param source: source of doi(Pubmed, RSS Feed, Cross ref)
            :param pmid: PubMed ID
            :param doi: Doi
            :param title: title variable
            :param connection_object: Connection object.cursor()
            :return: Cursor object or None
            """
    # Data insertion into the database
    try:
        with connection_object:
            connection_object.execute("INSERT INTO DOIs(Doi, PMID, Title, Abstract, Source, Filename, Created) VALUES(?, NULL, ?, NULL, NULL, ?, ?)",
                                      (doi, title, filename, datetime.now()))
            print("Successful DOI entry recorded!")
    except sqlite3.IntegrityError:
        print("Warning: Duplicate entry detected!")
        pass'''

'''def rss_parse_archive(file, key_id, doi):
    # TODO: Fix abstract parsing, but mainly UPDATING database if a title/abstract is found within the archive file

    """ given the correctly selected file, search for doi
                :param file: list of raw xml files stored as json
                :param key_id: id of doi within database for updating if title/abstract found
                :param doi: to scan for right doi
                :return: title/abstract, if both there or just title or nothing if not there
                """

    titles = []
    abstracts = []
    with open(file, "r") as f:
        data = f
        print(data)
        for key in data["entries"]:
            for val in key.values():
                if type(val) == str:
                    doi_search = re.search("(10\.\d{4,9}\/[-._;()/:A-Za-z0-9]+)", val)
                    if doi_search is not None and doi_search.group(0) == doi:
                        if key["title"]:
                            tag_match = re.compile(
                                r'(<!--.*?-->|<[^>]*>)|(\[{1}\bASAP\]{1}\s*)|(\bMarine\s\bDrugs\,\ \bVol\.\s[0-9]*\,\s\bPages\s[0-9]*\:\s*)')
                            clean_title = tag_match.sub('', key["title"])
                            titles.append(clean_title)
                        else:
                            print("no title")
                            # TODO: WORK ON ABSTRACT, not just summary, could be 'value' which is not in entries
                        if re.search(
                                '(^[A-Z][^.!?]*((\.|!|\?)(?! |\n|\r|\r\n)[^.!?]*)*(\.|!|\?)(?= |\n|\r|\r\n)\s?)(?:[A-Z][^.!?]*((\.|!|\?)(?! |\n|\r|\r\n)[^.!?]*)*(\.|!|\?)(?= |\n|\r|\r\n)\s)+',
                                key["summary"]):
                            abstract = key["summary"]
                            abstracts.append(abstract)
                        else:
                            print("no abstract")
    unique_titles = list(set(titles))
    unique_abstracts = list(set(abstracts))
    if unique_abstracts and unique_titles:
        return key_id, unique_titles[0], unique_abstracts[0]
    elif unique_titles:
        return key_id, unique_titles[0]
    else:
        return "no luck"'''
