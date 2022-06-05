#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#
# This file contains the functions to create and write
# the output files (CSV / JSON / HTML).
# The user can input a username to write in the output file
# the data related only to that user (and the output file will be
# twitterbot2-output/{username}.{csv,json,html}) or the word 'ALL'
# to write in the output file the data related to all the users
# in the database (and the output file will be
# twitterbot2-output/ALL.{csv,json,html}).
#

import logging
import os
import db
import csv
import json
import sys
import datetime

version_str = "0.1.8"


def version():
    return version_str


def print_version():
    print(version_str + "\n")


def print_banner():
    print(" _            _ _   _            _           _   ____")
    print("| |___      _(_) |_| |_ ___ _ __| |__   ___ | |_|___ \\")
    print("| __\\ \\ /\\ / / | __| __/ _ \\ '__| '_ \\ / _ \\| __| __) |")
    print("| |_ \\ V  V /| | |_| ||  __/ |  | |_) | (_) | |_ / __/")
    print(
        " \\__| \\_/\\_/ |_|\\__|\\__\\___|_|  |_.__/ \\___/ \\__|_____| "
        + version()
    )
    print("")
    print("       > edoardottt, https://www.edoardoottavianelli.it")
    print("       > https://github.com/edoardottt/twitterbot2")
    print("")


def tweet_banner(message):
    """
    This is a standard tweet to spread info about the bot.
    """
    tweet = str(datetime.datetime.now()) + "\n"
    tweet += "This is a bot at the service of @" + globals.user + ".\n"
    tweet += "https://github.com/edoardottt/twitterbot2\n"
    tweet += message + "\n"
    return tweet


logger = logging.getLogger("__main__")


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
        sys.exit()
    else:
        create_output_folder()
        filename = create_output_file(user + ".csv")
        with open(filename, "w", newline="") as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            for elem in values:
                wr.writerow(elem)
    logger.info("All data has been written into " + filename)


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
        sys.exit()
    else:
        create_output_folder()
        filename = create_output_file(user + ".json")

        dict = {}
        for elem in values:
            if not elem[0] in dict.keys():
                dict[elem[0]] = {}
            dict[elem[0]][elem[1]] = {
                "tweets": elem[2],
                "likes": elem[3],
                "retweets:": elem[4],
                "followers:": elem[5],
            }
        with open(filename, "w") as f:
            json.dump(dict, f)
    logger.info("All data has been written into " + filename)


def banner_html():
    banner = """<html>
    <head>
        <title>Twitterbot2 output</title>
    <style>
    * {
  box-sizing: border-box;
  font-family: Arial, Helvetica, sans-serif;
}

body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

/* Style the top navigation bar */
.topnav {
  overflow: hidden;
  background-color: #333;
}

/* Style the topnav links */
.topnav a {
  float: left;
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* Change color on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Style the content */
.content {
  background-color: #ddd;
  padding: 10px;
  height: 200px;
}

/* Style the footer */
.footer {
  background-color: #f1f1f1;
  padding: 10px;
  bottom: 0;
  text-align:center;
  width: 100%;
  position: fixed;
}
</style>
    </head>
    <body>
    <div class="topnav">
    <a href="https://github.com/edoardottt/twitterbot2">Twitterbot2 on GitHub</a>
    <a href="https://github.com/edoardottt/twitterbot2#contributing-">Contribute</a>
    <a href="https://github.com/edoardottt/twitterbot2/blob/main/README.md">Docs</a>
    <a href="https://github.com/edoardottt/twitterbot2/blob/main/LICENSE">License</a>
    </div>
    """
    return banner


def footer_html():
    footer = """<div class="footer">
        <p>twitterbot2 by <a href='https://github.com/edoardottt'>@edoardottt</a></p>
    </div>
    <br><br><br><br><br><br><br><br>
    </body>
    </html>
    """
    return footer


def html_table(lol):
    out_string = """<table border="1" cellspacing="15"><th scope="col">User</th>
    <th scope="col">Date</th>
    <th scope="col">Tweets</th>
    <th scope="col">Likes</th>
    <th scope="col">Retweets</th>
    <th scope="col">Followers</th>"""
    for sublist in lol:
        out_string += "  <tr><td>"
        out_string += "    </td><td>".join(list(map(str, sublist)))
        out_string += "  </td></tr>"
    out_string += "</table>"
    return out_string


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
        sys.exit()
    else:
        create_output_folder()
        filename = create_output_file(user + ".html")
        with open(filename, "w") as f:
            f.write(banner_html())
            f.write(html_table(values))
            f.write(footer_html())
    logger.info("All data has been written into " + filename)


def data_json(values):
    """
    This function tranforms the input values
    in a py dictionary useful for json.
    """
    dict = {}
    for elem in values:
        if not elem[0] in dict.keys():
            dict[elem[0]] = {}
        dict[elem[0]][elem[1]] = {
            "tweets": elem[2],
            "likes": elem[3],
            "retweets:": elem[4],
            "followers:": elem[5],
        }
    return dict


def usage():
    """
    usage: twitterbot2.py [-h] [-v | -t | -k KEYWORD | -nu | -nl | -nr \
| -s STATS | -oc OUTPUT_CSV | -oj OUTPUT_JSON | -oh OUTPUT_HTML]

    Twitterbot v2

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         Show the version of this program.
      -t, --timeline        Search for tweets in the bot and user's timeline.
      -k KEYWORD, --keyword KEYWORD
                            Search for tweets with defined keyword(s). If more than one,
                            comma separated enclosed in double quotes.
      -nu, --no-user        Don't like and retweet user tweets.
      -nl, --no-like        Don't like tweets, just retweet.
      -nr, --no-retweet     Don't retweet tweets, just like.
      -s STATS, --stats STATS
                            Show the statistics of the inputted bot (username).
      -oc OUTPUT_CSV, --output-csv OUTPUT_CSV
                            Produce a csv file containing the stats for the inputted used (ALL for anyone).
      -oj OUTPUT_JSON, --output-json OUTPUT_JSON
                            Produce a json file containing the stats for the inputted used (ALL for anyone).
      -oh OUTPUT_HTML, --output-html OUTPUT_HTML
                            Produce a html file containing the stats for the inputted used (ALL for anyone).
    """
    print("usage: twitterbot2.py [-h] [-v | -t | -k KEYWORD | -s]")
    print("")
    print("Twitterbot v2")
    print("")
    print("optional arguments:")
    print("  -h, --help     show this help message and exit")
    print("  -v, --version  Show the version of this program.")
    print("  -t, --timeline  Search for tweets in the bot and user's timeline.")
    print("  -k KEYWORD, --keyword KEYWORD")
    print(
        "                        Search for tweets with defined keyword(s). If more than one,"
    )
    print("                        comma separated enclosed in double quotes.")
    print("  -nu, --no-user     Don't like and retweet user tweets.")
    print("  -nl, --no-like     Don't like tweets, just retweet.")
    print("  -nr, --no-retweet  Don't retweet tweets, just like.")
    print("  -s STATS, --stats STATS")
    print("                        Show the statistics of the inputted bot (username).")
    print("  -oc OUTPUT_CSV, --output-csv OUTPUT_CSV")
    print(
        "                        Produce a csv file containing the stats for the inputted used (ALL for anyone)."
    )
    print("  -oj OUTPUT_JSON, --output-json OUTPUT_JSON")
    print(
        "                        Produce a json file containing the stats for the inputted used (ALL for anyone)."
    )
    print("  -oh OUTPUT_HTML, --output-html OUTPUT_HTML")
    print(
        "                        Produce a html file containing the stats for the inputted used (ALL for anyone)."
    )
