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
import sqlite3

db_filename = "database.db"

db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)  # connect to the database or create it


# ctreate table with the sql code input
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)


sql_create_analytics_table = """CREATE TABLE IF NOT EXISTS analytics (
                                    username text NOT NULL,
                                    date date NOT NULL,
                                    likes integer NOT NULL,
                                    retweets integer NOT NULL,
                                    followers integer NOT NULL,
                                    PRIMARY KEY (username,date)
                                );"""
if conn is not None:
    create_table(conn, sql_create_analytics_table)
conn.close()
