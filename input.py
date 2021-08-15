#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
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
        "-k",
        "--keyword",
        action="store_true",
        help="Search for tweets with a defined keyword.",
    )

    group.add_argument(
        "-s", "--stats", action="store_true", help="Show the statistics of the bot."
    )

    args = parser.parse_args()

    return args
