#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#
# This file handles the input from the standard input
# and return the arguments object (using argparse).
#
# twitterbot2.py [-h] [-v | -t | -k KEYWORD | -s STATS | -oc OUTPUT_CSV | -oj OUTPUT_JSON | -oh OUTPUT_HTML]
#
#


import argparse


def get_args():
    """
    Return the arguments provided by the user.
    """

    parser = argparse.ArgumentParser(description="Twitterbot v2")
    group = parser.add_mutually_exclusive_group(required=False)

    group.add_argument(
        "-v", "--version", action="store_true", help="Show the version of this program."
    )

    group.add_argument(
        "-t",
        "--timeline",
        action="store_true",
        help="Search for tweets in the bot and user's timeline.",
    )

    group.add_argument(
        "-k",
        "--keyword",
        type=str,
        help="Search for tweets with a defined keyword.",
    )

    group.add_argument(
        "-s",
        "--stats",
        type=str,
        help="Show the statistics of the inputted bot (username).",
    )

    group.add_argument(
        "-oc",
        "--output-csv",
        type=str,
        help="Produce a csv file containing the stats for the inputted used (ALL for anyone).",
    )

    group.add_argument(
        "-oj",
        "--output-json",
        type=str,
        help="Produce a json file containing the stats for the inputted used (ALL for anyone).",
    )

    group.add_argument(
        "-oh",
        "--output-html",
        type=str,
        help="Produce a html file containing the stats for the inputted used (ALL for anyone).",
    )

    args = parser.parse_args()

    return args
