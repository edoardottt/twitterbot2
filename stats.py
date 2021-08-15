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

try:
    import matplotlib.pyplot as plt

    plt.figure(num="twitterbot2 stats")
except Exception:
    print("Execute: pip install -r requirements.txt")
    sys.exit()

db_filename = "database.db"
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)


def check_stat(username, password):
    """
    This function checks the statistics for a user
    """
    timestamps = []  # contains all the timestamps saved in the records
    likes = []  # contains all the likes saved in the records
    retweets = []  # contains all the retweets saved in the records
    followers = []  # contains all the followers saved in the records
    d_likes = {}  # dictionary with as keys = days & values = likes
    d_retweets = {}  # dictionary with as keys = days & values = retweets
    d_followers = {}  # dictionary with as keys = days & values = followers
    if db_is_new:
        print("No database detected.")
        print("Execute the initdb.py file by typing in your command line:")
        print("python init_db.py")
        sys.exit()
    else:
        cursor = conn.cursor()
        # check if that user is in the database
        cursor.execute("SELECT * FROM users WHERE username = ?", (username))
        data = cursor.fetchone()
        if data is None:
            print("There aren't data for this username.")
            sys.exit()
        # if that user exists
        cursor.execute("SELECT * FROM analytics WHERE username = ?", (username,))
        data = cursor.fetchall()
        if data is not None:
            if len(data) != 0:
                for record in data:
                    timestamps += [record[1]]  # save the timestamp
                    likes += [int(record[2])]  # save the likes count
                    retweets += [int(record[3])]  # save the retweets count
                    followers += [int(record[4])]  # save the followers count
                # In this for loop all the arrays here declared become dictionary in this way:
                # All the likes, followers and retweets counts are aggregate per day.
                # Remember timestamps[:-16] means yyyy-mm-dd
                for i in range(len(timestamps)):
                    if not (timestamps[i][:-16] in d_likes):
                        for j in range(len(timestamps)):
                            if timestamps[i][:-16] == timestamps[j][:-16]:
                                if timestamps[i][:-16] in d_likes:
                                    d_likes[timestamps[i][:-16]] += likes[j]
                                else:
                                    d_likes[timestamps[i][:-16]] = likes[j]
                                if timestamps[i][:-16] in d_retweets:
                                    d_retweets[timestamps[i][:-16]] += retweets[j]
                                else:
                                    d_retweets[timestamps[i][:-16]] = retweets[j]
                                if timestamps[i][:-16] in d_followers:
                                    d_followers[timestamps[i][:-16]] -= d_followers[
                                        timestamps[i][:-16]
                                    ]
                                    d_followers[timestamps[i][:-16]] = followers[j]
                                else:
                                    d_followers[timestamps[i][:-16]] = followers[j]
                # adjust plot settings
                plt.subplots_adjust(bottom=0.2)
                plt.xticks(rotation=70)
                ax = plt.gca()
                ax.xaxis_date()
                date = list(d_likes.keys())
                likes_vector = [d_likes[i] for i in date]
                retweets_vector = [d_retweets[i] for i in date]
                followers_vector = [d_followers[i] for i in date]
                plt.plot(date, likes_vector, "-r", marker="o", label="likes")
                plt.plot(date, retweets_vector, "-g", marker="o", label="retweets")
                plt.plot(date, followers_vector, "-b", marker="o", label="followers")
                # if first > last element so the legend is shown on the right. Otherwise It's shown on the left
                if (
                    d_likes[list(d_likes.keys())[0]]
                    > d_likes[list(d_likes.keys())[len(d_likes) - 1]]
                ):
                    plt.legend(loc="upper right")
                else:
                    plt.legend(loc="upper left")
                # Print the results
                print("Total likes: " + str(sum(likes)))
                print("Total retweets: " + str(sum(retweets)))
                # add the number label in all points
                for var_date, var_likes in zip(date, likes_vector):
                    plt.text(var_date, var_likes, str(var_likes))
                for var_date, var_retweets in zip(date, retweets_vector):
                    plt.text(var_date, var_retweets, str(var_retweets))
                for var_date, var_followers in zip(date, followers_vector):
                    plt.text(var_date, var_followers, str(var_followers))
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
                print("There aren't data for this username.")
    conn.close()
