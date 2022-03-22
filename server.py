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
# This file contains the backend code and
# API logic for the web service.
#

from flask import Flask
from flask import request
from flask.templating import render_template
import datetime
import db
from dateutil.parser import parse
import threading

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = "ILVYilvbthLQETHeteggrgwi2r389"

# Needed for uptime
starting_time = datetime.datetime.now()


@app.route("/")
def hello():
    conn = db.conn_db()
    users = db.all_users(conn)
    return render_template("index.html", len=len(users), users=users)


def user_ok(user):
    """
    This function checks if a username is correct.
    """
    if user is None:
        return False
    if len(user) == 0:
        return False
    conn = db.conn_db()
    users = db.all_users(conn)
    for param in users:
        if user == param[0]:
            return True
    return False


@app.route("/dashboard")
def user_dashboard():
    user = request.args.get("user")
    if not user_ok(user):
        return render_template("error.html", errormsg="Invalid username.")

    # if user ok ->
    conn = db.conn_db()
    values = db.today_stats(conn, user)
    today_show = 1
    if values is None:
        today_show = 0
    else:
        (
            username,
            today,
            tweet_count,
            likes_count,
            retweet_count,
            followers_count,
        ) = values

    values = db.user_stats(conn, user)
    if values is None:
        return render_template("error.html", errormsg="No data for this user.")

    # render last 50 logs
    logs_line = 50
    logs = []
    render_logs = 1
    try:
        with open("twitterbot2.log", "r") as f:
            text = f.read().split("\n")
        if len(text) > logs_line:
            start = len(text) - logs_line - 1
        else:
            start = 0
        for line in text[start:]:
            if line.strip() != "":
                logs.append(line)
    except Exception:
        render_logs = 0

    if not today_show:
        (
            tweet_count,
            likes_count,
            retweet_count,
            followers_count,
        ) = ("", "", "", "")

    uptime = "🟢Uptime: " + str(datetime.datetime.now() - starting_time)
    for thread in threading.enumerate():
        if thread.getName() == "bot":
            if not thread.is_alive():
                uptime = "🔴Uptime: Dead"
                break

    return render_template(
        "dashboard.html",
        user=user,
        update=datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"),
        tweets=tweet_count,
        likes=likes_count,
        retweets=retweet_count,
        followers=followers_count,
        values=values,
        today_show=today_show,
        len=len(logs),
        logs=logs,
        render_logs=render_logs,
        uptime=str(uptime).split(".")[0],
    )


# ---------------------------------------------------------
# ------------------------ API ----------------------------
# ---------------------------------------------------------

@app.route("/api/health")
def api_health():
    """
    Server health endpoint.
    """
    for thread in threading.enumerate():
        if thread.getName() == "bot" and not thread.is_alive():
            return "error"
    return "ok"


@app.route("/api/tweets/<user>")
def api_user_tweets(user):
    """
    Total tweets for user <user>.
    """
    if not user_ok(user):
        return "ERROR: Invalid username."

    # if user ok ->
    conn = db.conn_db()
    values = db.user_stats(conn, user)
    if values is None:
        return "ERROR: No data for this user."
    else:
        result = 0
        for i in range(0, len(values)):
            result += values[i][2]
        return str(result)


@app.route("/api/likes/<user>")
def api_user_likes(user):
    """
    Total likes for user <user>.
    """
    if not user_ok(user):
        return "ERROR: Invalid username."

    # if user ok ->
    conn = db.conn_db()
    values = db.user_stats(conn, user)
    if values is None:
        return "ERROR: No data for this user."
    else:
        result = 0
        for i in range(0, len(values)):
            result += values[i][3]
        return str(result)


@app.route("/api/retweets/<user>")
def api_user_retweets(user):
    """
    Total retweets for user <user>.
    """
    if not user_ok(user):
        return "ERROR: Invalid username."

    # if user ok ->
    conn = db.conn_db()
    values = db.user_stats(conn, user)
    if values is None:
        return "ERROR: No data for this user."
    else:
        result = 0
        for i in range(0, len(values)):
            result += values[i][4]
        return str(result)


@app.route("/api/followers/<user>")
def api_user_followers(user):
    """
    Latest follower count for user <user>.
    """
    if not user_ok(user):
        return "ERROR: Invalid username."

    # if user ok ->
    conn = db.conn_db()
    values = db.user_stats(conn, user)
    if values is None:
        return "ERROR: No data for this user."
    else:
        result = values[len(values) - 1][5]
        return str(result)


def string_to_date(date):
    """
    @Input: string
    @Output: string
    This function tries to convert a string into a date,
    if it's not possible return an empty string.
    """
    try:
        converted = parse(date)
        return converted
    except Exception:
        return ""


@app.route("/api/tweets/<user>/<date>")
def api_user_date_tweets(user, date):
    """
    Tweets for user <user> in date <date>.
    Date format: YYYY-MM-DD.
    """
    if not user_ok(user):
        return "ERROR: Invalid username."
    if string_to_date(date) == "":
        return "ERROR: Invalid date."
    # if checks ok ->
    conn = db.conn_db()
    values = db.user_date_stats(conn, user, date)
    if values is None or len(values) == 0:
        return "ERROR: No data for this user on this day."
    else:
        result = values[0][2]
        return str(result)


@app.route("/api/likes/<user>/<date>")
def api_user_date_likes(user, date):
    """
    Likes for user <user> in date <date>.
    Date format: YYYY-MM-DD.
    """
    if not user_ok(user):
        return "ERROR: Invalid username."
    if string_to_date(date) == "":
        return "ERROR: Invalid date."
    # if checks ok ->
    conn = db.conn_db()
    values = db.user_date_stats(conn, user, date)
    if values is None or len(values) == 0:
        return "ERROR: No data for this user on this day."
    else:
        result = values[0][3]
        return str(result)


@app.route("/api/retweets/<user>/<date>")
def api_user_date_retweets(user, date):
    """
    Retweets for user <user> in date <date>.
    Date format: YYYY-MM-DD.
    """
    if not user_ok(user):
        return "ERROR: Invalid username."
    if string_to_date(date) == "":
        return "ERROR: Invalid date."
    # if checks ok ->
    conn = db.conn_db()
    values = db.user_date_stats(conn, user, date)
    if values is None or len(values) == 0:
        return "ERROR: No data for this user on this day."
    else:
        result = values[0][4]
        return str(result)


@app.route("/api/followers/<user>/<date>")
def api_user_date_followers(user, date):
    """
    Followers for user <user> in date <date>.
    Date format: YYYY-MM-DD.
    """
    if not user_ok(user):
        return "ERROR: Invalid username."
    if string_to_date(date) == "":
        return "ERROR: Invalid date."
    # if checks ok ->
    conn = db.conn_db()
    values = db.user_date_stats(conn, user, date)
    if values is None or len(values) == 0:
        return "ERROR: No data for this user on this day."
    else:
        result = values[0][5]
        return str(result)


if __name__ == "__main__":
    app.run()
