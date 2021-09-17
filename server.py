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
from random import randint

from flask.templating import render_template

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = "ILVYilvbthLQETHeteggrgwi2r389"


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/<user>")
def user_dashboard(user):
    randvalue = randint(0, 2722235)
    return render_template("dashboard.html", user=user, random=randvalue)


if __name__ == "__main__":
    app.run()
