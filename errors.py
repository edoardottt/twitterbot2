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
import twitter
import urllib


def error_handler(e):
    """
    This function handles all the twitterbot2 errors
        - twitter.api.TwitterHTTPError
        - urllib.error.URLError
        - generic
    """

    logger = logging.getLogger("__main__")
    if e.__class__ == twitter.api.TwitterHTTPError:
        logger.error(f"{str(e.e)} on {e.uri}")

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
    elif e.__class__ == urllib.error.URLError:
        logger.error(str(e.reason))
        logger.info("Sleeping for five minutes.")
        time.sleep(5 * 60)

    else:
        logger.info("Sleeping for ten seconds.")
        time.sleep(10)
