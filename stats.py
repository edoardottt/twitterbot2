#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#


import os
import sys
import sqlite3
import globals
import logging

try:
    import matplotlib.pyplot as plt

    plt.figure(num="Twitterbot2 - " + globals.bot_user + " stats")
except Exception:
    logger = logging.getLogger(__name__)
    logger.error("Execute: pip install -r requirements.txt")
    sys.exit()

db_filename = "database.db"
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)


def check_stat(username):
    """
    This function checks the statistics for the inputted user
    """
    logger = logging.getLogger("matplotlib")
    logger.setLevel(logging.CRITICAL)
    dates = []  # contains all the dates stored in the database
    tweets = []  # contains all the tweets stored in the database
    likes = []  # contains all the likes stored in the records
    retweets = []  # contains all the retweets stored in the records
    if db_is_new:
        logger = logging.getLogger(__name__)
        logger.error("No database detected.")
        logger.error("Execute the initdb.py file by typing in your command line:")
        logger.error("python init_db.py")
        sys.exit()
    else:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM statistics WHERE username = ?", (username,))
        data = cursor.fetchall()
        if data is not None and len(data) != 0:
            for record in data:
                dates += [record[1]]  # save the timestamp
                tweets += [int(record[2])]  # save the tweets count
                likes += [int(record[3])]  # save the likes count
                retweets += [int(record[4])]  # save the retweets count
            # adjust plot settings
            plt.subplots_adjust(bottom=0.2)
            plt.xticks(rotation=70)
            ax = plt.gca()
            ax.xaxis_date()
            plt.plot(dates, tweets, "-r", marker="o", label="tweets")
            plt.plot(dates, likes, "-g", marker="o", label="likes")
            plt.plot(dates, retweets, "-b", marker="o", label="retweets")
            # if first > last element the legend is shown on the right, otherwise it's shown on the left
            if tweets[0] > tweets[len(tweets) - 1]:
                plt.legend(loc="upper right")
            else:
                plt.legend(loc="upper left")
            # Print the results
            logger = logging.getLogger(__name__)
            logger.info("Total tweets: " + str(sum(tweets)))
            logger.info("Total likes: " + str(sum(likes)))
            logger.info("Total retweets: " + str(sum(retweets)))
            plt.title("Statistics for " + username)
            plt.subplots_adjust(
                left=None,
                bottom=0.13,
                right=0.98,
                top=0.94,
                wspace=None,
                hspace=None,
            )
            plt.show()
        else:
            logger = logging.getLogger(__name__)
            logger.warning("There aren't data for this username.")
    conn.close()
