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
# username text NOT NULL
# date date NOT NULL
# tweets integer NOT NULL
# likes integer NOT NULL
# retweets integer NOT NULL
#
# PRIMARY KEY (username, date)

import os
import sqlite3
import sys
import datetime
import logging


def conn_db():
    """
    This function returns a connection to the database.
    """
    db_filename = "database.db"
    db_is_new = not os.path.exists(db_filename)
    if db_is_new:
        logger = logging.getLogger(__name__)
        logger.error("You must execute: python init_db.py")
        sys.exit()
    conn = sqlite3.connect(db_filename)
    return conn


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
    sql = """ UPDATE statistics SET tweets = ?, likes = ?, retweets = ? WHERE username = ? AND date = ? """
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()


def today_stats(conn, username):
    """
    This function retrieves the record of today with up-to-date values.
    """
    sql = """ SELECT * FROM statistics WHERE username = ? AND date = ? """
    cur = conn.cursor()
    cur.execute(
        sql,
        (
            username,
            datetime.datetime.today().strftime("%Y-%m-%d"),
        ),
    )
    values = cur.fetchone()
    return values


def user_stats(conn, username):
    """
    This function retrieves all the records for a user.
    """
    sql = """ SELECT * FROM statistics WHERE username = ? """
    cur = conn.cursor()
    cur.execute(sql, (username,))
    values = cur.fetchall()
    return values


def all_stats(conn):
    """
    This function retrieves all the records.
    """
    sql = """ SELECT * FROM statistics """
    cur = conn.cursor()
    cur.execute(sql)
    values = cur.fetchall()
    return values
