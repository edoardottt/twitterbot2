#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#


def usage():
    """
    usage: twitterbot2.py [-h] [-v | -t | -k KEYWORD | -s]

    Twitterbot v2

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         Show the version of this program.
      -t, --timeline        Search for tweets in the bot and user's timeline.
      -k KEYWORD, --keyword KEYWORD
                            Search for tweets with a defined keyword.
      -s STATS, --stats STATS
                        Show the statistics of the inputted bot (username).
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
    print("                      Search for tweets with a defined keyword.")
    print("  -s STATS, --stats STATS")
    print("                  Show the statistics of the inputted bot (username).")
