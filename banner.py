#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#
# This file provides the function to print the banner
# in the standard output and a banner tweet sample.
#


import version
import datetime
import globals


def print_banner():
    print(" _            _ _   _            _           _   ____")
    print("| |___      _(_) |_| |_ ___ _ __| |__   ___ | |_|___ \\")
    print("| __\\ \\ /\\ / / | __| __/ _ \\ '__| '_ \\ / _ \\| __| __) |")
    print("| |_ \\ V  V /| | |_| ||  __/ |  | |_) | (_) | |_ / __/")
    print(
        " \\__| \\_/\\_/ |_|\\__|\\__\\___|_|  |_.__/ \\___/ \\__|_____| "
        + version.version()
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
