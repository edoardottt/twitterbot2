#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#
#
# This file contains the logic when a new TwitterHTTPError
# happens.
#

import time
import logging


def error_handler(e):
    """
    This function handles all the TwitterHTTPError errors
    """
    logger = logging.getLogger("__main__")
    logger.error(str(e.e) + " on " + e.uri)

    # == 429 TOO MANY REQUESTS -> Sleep for one hour
    if str(e.e.code) == "429":
        logger.info("Sleeping for one hour.")
        time.sleep(60 * 60)
        return

    # == 403 FORBIDDEN -> Sleep for ten seconds
    if str(e.e.code) == "403":
        logger.info("Sleeping for ten seconds.")
        time.sleep(10)
        return

    # for other types of issues with specific behaviour
    # add here an additional handler

    # == DEFAULT ==
    logger.info("Sleeping for ten seconds.")
    time.sleep(10)
