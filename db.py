#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#


def create_stat(conn, data):
    """
    This function creates a record in the statistics table.
    """
    sql = """ INSERT INTO statistics VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
