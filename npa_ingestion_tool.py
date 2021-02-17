# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:56:42 2021

@author: maras
"""

from datetime import datetime
from metapub import PubMedFetcher
from bs4 import BeautifulSoup
import feedparser
import json
import re
import sqlite3
import requests


def no_newline(line):
    """ Takes string input and checks if blank or not
                    :param line: string
                    :return: returns boolean of true for a blank, false if not blank
                    """
    new_line = line.rstrip('\n')
    replace_line = new_line.replace("/", "").replace(".", "").replace(":", "").replace("-", "").replace(
        "=", "").replace(
        "!", "").replace("@", "").replace("#", "").replace(
        "$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")
    return replace_line


def blanks(string):
    """ Takes string input and checks if blank or not
                :param string: string
                :return: returns boolean of true for a blank, false if not blank
                """
    if string == "":
        return True
    else:
        return False

# Nothing useful for all links, cannot find or irrelevant info like CAPTCHA requests. All getting unicode errors
'''def get_xml(url, archive_filename):
    """ parse a xml file retrieved with requests using feedparser to the gather list of DOIs from the
                    specified xml
                :param url: url of rss feed
                :param archive_filename: The file name of the archive file
                :return: raw string of text from requests.get(url)
                """
    url_request = requests.get(url)
    raw_xml_str = url_request.text
    path = 'C:/Users/maras/Desktop/NPA_Ingestion_Tool/raw_xml_archive/' + archive_filename
    with open(path, "w") as f:
        json.dump(raw_xml_str, f) # f.write(raw_xml_str.text)
    return raw_xml_str'''


def parse_rss(url, archive_file):
    """ parse a xml file retrieved with requests using feedparser to the gather list of DOIs from the
                specified xml
            :param archive_file: name of raw feed parser file
            :param url: url of RSS feed
            :return: list of unique DOIs
            """
    # Parse RSS url w/ feedparser to get consistent format
    rss_feed = feedparser.parse(url)

    # Creation of JSON file for easy viewing
    path = 'C:/Users/maras/Desktop/NPA_Ingestion_Tool/raw_xml_archive/' + archive_file
    with open(path, "x") as f:
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
                    # print(doi_search.group(1))
                    break

    # Remove duplicate DOIs from list
    unique_doi_list = list(set(doi_list))
    return archive_file, unique_doi_list


def doi_2_pmid(doi):
    """ returns PMID for a given DOI
                    :param doi:  DOI as string
                    :return: PMID as string
                    """
    fetch = PubMedFetcher()
    pm_id = fetch.pmids_for_query(f"{doi}[DOI]")
    return pm_id


def pmid_2_abstract(pm_id):
    """ returns abstract for a given pmid
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


# SQLite3 Database Functions
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
        "CREATE TABLE IF NOT EXISTS DOIs (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,Doi VARCHAR UNIQUE NOT NULL, PMID VARCHAR, Title VARCHAR, Abstract VARCHAR, Source VARCHAR, Filename NOT NULL, Created NOT NULL)")
    return cursor


def sqlite3_insertion(connection_object, doi, pmid ,title, abstract, source, filename):
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
            connection_object.execute("INSERT INTO DOIs(Doi, PMID, Title, Abstract, Source, Filename, Created) VALUES(?, ?, ?, ?, ?, ?, ?)",
                                      (doi, pmid, title, abstract, source, filename, datetime.now()))

    except sqlite3.IntegrityError:
        print("Warning: Duplicate entry detected!")
        pass


def sqlite3_insertion_no_abstract(connection_object, doi, pmid ,title, source, filename):
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
            connection_object.execute("INSERT INTO DOIs(Doi, PMID, Title, Abstract, Source, Filename, Created) VALUES(?, ?, ?, NULL, ?, ?, ?)",
                                      (doi, pmid, title, source, filename, datetime.now()))

    except sqlite3.IntegrityError:
        print("Warning: Duplicate entry detected!")
        pass


def sqlite3_insertion_only_doi(connection_object, doi, filename):
    """ insert data into the SQLite3 database
            :param filename: name of archive file
            :param source: source of doi(Pubmed, RSS Feed, Cross ref)
            :param pmid: PubMed ID
            :param doi: Doi
            :param connection_object: Connection object.cursor()
            :return: None
            """
    # Data insertion into the database
    try:
        with connection_object:
            connection_object.execute("INSERT INTO DOIs(Doi, PMID, Title, Abstract, Source, Filename, Created) VALUES(?, NULL, NULL, NULL, NULL, ?, ?)",
                                      (doi, filename, datetime.now()))
    except sqlite3.IntegrityError:
        print("Warning: Duplicate entry detected!")
        pass


def sqlite3_update_pubmed_title_abstract(connection_object,  pm_id, title, abstract, source, ids):
    """ Update data in the SQLite3 database, when title/abstract found in PubMed
                :param ids: Primary Key ID
                :param pm_id: PubMed ID
                :param source: source of title.abstract
                :param abstract: article abstract
                :param title: article title
                :param connection_object: Connection object.cursor()
                :return: None
                """
    try:
        connection_object.execute("UPDATE DOIs SET PMID = ?, Title = ?, Abstract = ?, Source = ? WHERE ID = ?", (pm_id, title, abstract, source, ids))

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)


def sqlite3_update_pubmed_title_only(connection_object, pm_id, title, source, ids):
    """ Update data in the SQLite3 database, when Pubmed only has title
                  :param ids: Primary Key ID
                  :param pm_id: PubMed ID
                  :param source: source of title.abstract
                  :param title: article title
                  :param connection_object: Connection object.cursor()
                  :return: None
                  """
    try:
        connection_object.execute("UPDATE DOIs SET PMID = ?, Title = ?, Source = ? WHERE ID = ?", (pm_id, title, source, ids))

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)


def doi_date_locator(cursor_statement):
    """ Queries database for 3 week old DOIs for id, doi and the date
                        :param cursor_statement: cursor object
                        :return: list of dictionaries that contains id, doi and date
                        """
    select_statement = cursor_statement.execute(
        "SELECT * FROM DOIs WHERE Abstract IS NULL and Created <= date('now', '-21 day')")

    date_hits = [{"id": row[0], "doi": row[1], "file": row[6]} for row in select_statement]
    return date_hits


def rss_parse_archive(file, key_id, doi):
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
        data = json.load(f)
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
        return ("no luck")
