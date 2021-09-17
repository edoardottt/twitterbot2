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
# This file contains the api logic for the web service.
#

from flask import Flask
from flask import request
import db
from random import randint

from flask.templating import render_template

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = "ILVYilvbthLQETHeteggrgwi2r389"


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

    randvalue = randint(0, 100)
    return render_template("dashboard.html", user=user, random=randvalue)


if __name__ == "__main__":
    app.run()
