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
import sys

logger = logging.getLogger(__name__)


def create_output_folder():
    """
    This function creates (only if not exists already) the
    `twitterbot2-output` folder.
    """
    directory = "twitterbot2-output"
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_output_file(filename):
    """
    This function creates (only if not exists already) the
    output file in the `twitterbot2-output` folder.
    """
    directory = "twitterbot2-output"
    if not os.path.exists(directory + "/" + filename):
        _ = open(directory + "/" + filename, "w+")
    else:
        answer = ask_confirmation()
        if not answer:
            sys.exit()
        else:
            _ = open(directory + "/" + filename, "w+")
    return directory + "/" + filename


def ask_confirmation():
    """
    This function checks if the user wants to override the already
    existing output file.
    """
    answer = str(input("The file already exists. Do you want to override? (Y/n)"))
    if answer.lower() == "y" or answer.lower() == "yes" or answer.lower() == "":
        return True
    return False


def output_csv(user):
    """
    This function writes in the CSV output file the results got
    from the database for the specified user or for all of them
    (if ALL is inputted).
    """
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
    """
    This function writes in the JSON output file the results got
    from the database for the specified user or for all of them
    (if ALL is inputted).
    """
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

        dict = {}
        for elem in values:
            dict[elem[1]] = {"tweets": elem[2], "likes": elem[3], "retweets:": elem[4]}
        with open(filename, "w") as f:
            json.dump(dict, f)


def output_html(user):
    """
    This function writes in the HTML output file the results got
    from the database for the specified user or for all of them
    (if ALL is inputted).
    """
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
        print(filename)
