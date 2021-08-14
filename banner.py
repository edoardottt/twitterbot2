#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#


import version
import datetime


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


def tweet_banner():
    tweet = str(datetime.datetime.now()) + "\n"
    tweet += "This is a bot at the service of the only almighty God @edoardottt2.\n"
    tweet += "https://www.edoardoottavianelli.it\n"
    tweet += "https://github.com/edoardottt\n"
    tweet += "https://twitter.com/edoardottt2"
    return tweet
