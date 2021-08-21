#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#

# TABLE statistics:
#
# username text NOT NULL,
# date date NOT NULL,
# likes integer NOT NULL,
# retweets integer NOT NULL,
# followers integer NOT NULL,
# PRIMARY KEY (username, date)


def create_stat(conn, data):
    """
    This function creates a record in the statistics table.
    """
    sql = """ INSERT INTO statistics VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()


def update_stat(conn, data):
    """
    This function updates the record of today with new up-to-date values.
    """
    sql = """ UPDATE statistics SET likes = ?, retweets = ?, followers = ? WHERE username = ? AND date = ? """
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
