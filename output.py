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
import json

logger = logging.getLogger(__name__)


def create_output_folder():
    directory = "twitterbot2-output"
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_output_file(filename):
    directory = "twitterbot2-output"
    if not os.path.exists(directory + "/" + filename):
        _ = open(directory + "/" + filename, "w+")
    return directory + "/" + filename


def output_csv(user):
    conn = db.conn_db()
    if user == "ALL":
        values = db.all_stats(conn)
    else:
        values = db.user_stats(conn, user)
    if len(values) == 0:
        logger.warning("There aren't data for this user.")
    else:
        create_output_folder()
        filename = create_output_file(user + ".csv")
        with open(filename, "w", newline="") as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            for elem in values:
                wr.writerow(elem)


def output_json(user):
    conn = db.conn_db()
    if user == "ALL":
        values = db.all_stats(conn)
    else:
        values = db.user_stats(conn, user)
    if len(values) == 0:
        logger.warning("There aren't data for this user.")
    else:
        create_output_folder()
        filename = create_output_file(user + ".json")
        json_string = json.dumps(values)
        with open(filename, "w") as f:
            json.dump(json_string, f)


def output_html(user):
    conn = db.conn_db()
    if user == "ALL":
        values = db.all_stats(conn)
    else:
        values = db.user_stats(conn, user)
    if len(values) == 0:
        logger.warning("There aren't data for this user.")
    else:
        create_output_folder()
        filename = create_output_file(user + ".html")
        pass
