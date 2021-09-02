# twitterbot2 🤖

**Follow me [edoardottt](https://twitter.com/edoardottt2)**

**Say Hi to [Son of Anton](https://twitter.com/ai_testing)**

![python-version](https://github.com/edoardottt/images/blob/main/twitterbot2/python-version.svg)
![linux-build-success-badge](https://github.com/edoardottt/images/blob/main/twitterbot2/linux-build-success-badge.svg)
![win-build-success-badge.svg](https://github.com/edoardottt/images/blob/main/twitterbot2/win-build-success-badge.svg)

Useful notes/links 🔗
--------

- https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api
- https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits

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

Contributing 🤝
--------

Just open an [issue](https://github.com/edoardottt/twitterbot2/issues)/[pull request](https://github.com/edoardottt/twitterbot2/pulls).

License 📝
--------

This repository is under [GPLv3 License](https://github.com/edoardottt/twitterbot2/blob/main/LICENSE).  
[edoardoottavianelli.it](https://www.edoardoottavianelli.it) to contact me.
