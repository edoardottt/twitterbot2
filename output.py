#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#

import logging
import os
import db
import csv

logger = logging.getLogger(__name__)


def create_output_folder():
    directory = "twitterbot-output"
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_output_file(filename):
    if not os.path.exists("twitterbot-output/" + filename):
        _ = open("twitterbot-output/" + filename, "w+")
    return "twitterbot-output/" + filename


def output_csv(user):
    create_output_folder()
    filename = create_output_file(user + ".csv")
    conn = db.conn_db()
    if user == "ALL":
        values = db.all_stats(conn)
    else:
        values = db.user_stats(conn, user)
    with open(filename, "w", newline="") as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for elem in values:
            wr.writerow(elem)


"""
def output_json(user):
    create_output_folder()
    filename = create_output_file(user + ".json")
    conn = db.conn_db()
    if user == "ALL":
        values = db.all_stats(conn)
    else:
        values = db.user_stats(conn, user)


def output_html(user):
    create_output_folder()
    filename = create_output_file(user + ".html")
    conn = db.conn_db()
    if user == "ALL":
        values = db.all_stats(conn)
    else:
        values = db.user_stats(conn, user)
"""
