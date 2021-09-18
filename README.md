<p align="center">
  <img src="https://github.com/edoardottt/images/blob/main/twitterbot2/twitterbot2.png"><br>
  <b>Simple bot for twitter.</b><br>
  <!--badges-->
  <a href="https://www.edoardoottavianelli.it"><img src="https://github.com/edoardottt/images/blob/main/twitterbot2/python-version.svg"/></a>
  <a href="https://www.edoardoottavianelli.it"><img src="https://github.com/edoardottt/images/blob/main/twitterbot2/linux-build-success-badge.svg"/></a>
  <a href="https://www.edoardoottavianelli.it"><img src="https://github.com/edoardottt/images/blob/main/twitterbot2/win-build-success-badge.svg"/></a>
  <a href="https://github.com/edoardottt/twitterbot2/actions/workflows/python-app.yml"><img src="https://github.com/edoardottt/twitterbot2/actions/workflows/python-app.yml/badge.svg"/></a>
  <br>
  <sub>
    Coded with 💙 by edoardottt.
  </sub>
  <br>
  <!--Tweet button-->
</p>

<p align="center">
  <a href="#description-">Description</a> •
  <a href="#installation-">Install</a> •
  <a href="#usage-">Usage</a> •
  <a href="#useful-noteslinks-">Notes</a> •
  <a href="#contributing-">Contributing</a> •
  <a href="#license-">License</a>
</p>

**twitterbot2 live demo running on [twitter.com/ai_testing](https://twitter.com/ai_testing)**

Description 🔦 
--------

Simple bot for Twitter. 2nd version of [twitterbot](https://github.com/edoardottt/twitterbot).

Installation 📡
-------

- `git clone https://github.com/edoardottt/twitterbot2`
- `cd twitterbot2`
- `pip install -r requirements.txt`
- Edit the `config.yaml` and `globals.py` files 
- `python init_db.py`
- `python twitterbot2.py -h`

Usage 🚀
-------

```
usage: twitterbot2.py [-h] [-v | -t | -k KEYWORD | -s STATS | -oc OUTPUT_CSV | -oj OUTPUT_JSON | -oh OUTPUT_HTML]

Twitterbot v2

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Show the version of this program.
  -t, --timeline        Search for tweets in the bot and user's timeline.
  -k KEYWORD, --keyword KEYWORD
                        Search for tweets with a defined keyword.
  -s STATS, --stats STATS
                        Show the statistics of the inputted bot (username).
  -oc OUTPUT_CSV, --output-csv OUTPUT_CSV
                        Produce a csv file containing the stats for the inputted used (ALL for anyone).
  -oj OUTPUT_JSON, --output-json OUTPUT_JSON
                        Produce a json file containing the stats for the inputted used (ALL for anyone).
  -oh OUTPUT_HTML, --output-html OUTPUT_HTML
                        Produce a html file containing the stats for the inputted used (ALL for anyone).
```

Useful notes/links 🔗
--------

- https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api
- https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits
- This app uses a Flask server. Do not expose this on the public Internet, use this behind NAT/firewall.

Contributing 🤝
--------

Just open an [issue](https://github.com/edoardottt/twitterbot2/issues)/[pull request](https://github.com/edoardottt/twitterbot2/pulls).  
Read also [Code of Conduct](https://github.com/edoardottt/twitterbot2/blob/main/CODE_OF_CONDUCT.md) and [Contributing](https://github.com/edoardottt/twitterbot2/blob/main/CONTRIBUTING.md) files.

License 📝
--------

This repository is under [GPLv3 License](https://github.com/edoardottt/twitterbot2/blob/main/LICENSE).  
[edoardoottavianelli.it](https://www.edoardoottavianelli.it) to contact me.
