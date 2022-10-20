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
# Moreover, it contains the function to retrieve
# the secrets form the config.yaml file.
#
# twitterbot2.py [-h] [-v | -t | -k KEYWORD | -s STATS | -oc OUTPUT_CSV | -oj OUTPUT_JSON | -oh OUTPUT_HTML]
#
#


import argparse
import yaml
import logging


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
        "-p", "--port", type=str, help="Set the port to be used (default 5555)."
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
        help="Search for tweets with defined keyword(s). If more than one, comma separated enclosed in double quotes.",
    )

    parser.add_argument(
        "-nu",
        "--no-user",
        action="store_true",
        help="Don't like and retweet user tweets.",
    )

    parser.add_argument(
        "-nl",
        "--no-like",
        action="store_true",
        help="Don't like tweets, just retweet.",
    )

    parser.add_argument(
        "-nr",
        "--no-retweet",
        action="store_true",
        help="Don't retweet tweets, just like.",
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


def read_secrets():
    """
    With this function we can read secrets
    from the configuration file.
    @return:
        {
            api_key
            api_secret_key
            bearer_token
            access_token
            access_token_secret
        }
    """
    with open("config.yaml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logger = logging.getLogger("__main__")
            logger.error(exc)
            exit()
