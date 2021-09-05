#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#
# This file contains all the functions related to
# the database (database.db).
# These functions are intended to create, read, update
# and delete data from the DB.
#

# TABLE statistics:
#
# username text NOT NULL
# date date NOT NULL
# tweets integer NOT NULL
# likes integer NOT NULL
# retweets integer NOT NULL
# followers integer NOT NULL
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
    sql = """ INSERT INTO statistics VALUES(?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()


def update_stat(conn, data):
    """
    This function updates the record of today with new up-to-date values.
    """
    sql = """ UPDATE statistics SET tweets = ?, likes = ?, retweets = ?,\
 followers = ? WHERE username = ? AND date = ? """
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


def month_stats(conn, username):
    """
    This function retrieves the values of the
    current month for a given user.
    """
    sql = """ SELECT sum(tweets), sum(likes), sum(retweets) FROM statistics \
        WHERE username = ? AND date >= ? AND date <= ? GROUP BY username """
    cur = conn.cursor()
    current_year = datetime.datetime.today().strftime("%Y")
    current_month = datetime.datetime.today().strftime("%m")
    starting_day = datetime.datetime.today().replace(day=1).strftime("%Y-%m-%d")
    february_days = 28
    if (
        int(current_year) % 4 == 0
        and int(current_year) % 100 != 0
        or int(current_year) % 400 == 0
    ):
        february_days = 29
    months = {
        1: 31,
        2: february_days,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    ending_day = (
        datetime.datetime.today()
        .replace(day=months[int(current_month)])
        .strftime("%Y-%m-%d")
    )
    cur.execute(
        sql,
        (
            username,
            starting_day,
            ending_day,
        ),
    )
    tweets, likes, retweets = cur.fetchone()
    return tweets, likes, retweets
