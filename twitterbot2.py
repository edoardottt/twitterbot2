#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#

import twitter
import secrets
import time
import globals
import logging
import banner

# from datetime import datetime


# ----------- global vars -------------
retweet_count = 0
tweet_count = 0
likes_count = 0
# -------------------------------------


def auth(token, token_secret, consumer_key, consumer_secret):
    """
    This function provides the authentication to twitter.
    token = access token
    token_secret = access secret token
    consumer_key = Api key
    consumer_secret = Api Secret key
    """
    t = twitter.Twitter(
        auth=twitter.OAuth(token, token_secret, consumer_key, consumer_secret)
    )
    return t


def get_home(t):
    # Get your "home" timeline
    return t.statuses.home_timeline()


def get_friend_home(t, name):
    # Get a particular friend's timeline
    return t.statuses.user_timeline(screen_name=name)


def tweet(t, message):
    # Update your status
    t.statuses.update(status=message)


def put_like(t, status):
    # Favorite/like a status
    if not status["favorited"]:
        logging.info("Put like on a tweet by {}".format(status["user"]["screen_name"]))
        t.favorites.create(_id=status["id"])


def search(t, term):
    # Search for the latest tweets about <term>
    return t.search.tweets(q=term)


banner.print_banner()

secretss = secrets.read_secrets()

bot = auth(
    secretss["access_token"],
    secretss["access_token_secret"],
    secretss["api_key"],
    secretss["api_secret_key"],
)


logging.basicConfig(
    encoding="utf-8", level=logging.DEBUG, format="%(asctime)s %(message)s"
)


while True:
    logging.info("Tweet count: " + str(tweet_count))
    logging.info("Likes count: " + str(tweet_count))
    home = get_home(bot)
    if home is not None:
        tweet_count += len(home)
    else:
        logging.warning("Rate limit exceeded")
        time.sleep(15 * 60)
    for tweet_home in home:
        # if tweet_home["user"]["screen_name"] == globals.user:
        put_like(bot, tweet_home)
        likes_count += 1
        time.sleep(2)

    logging.info("Sleeping for one minute.")
    time.sleep(60)

    home = get_friend_home(bot, globals.user)
    if home is not None:
        tweet_count += len(home)
    else:
        logging.warning("Rate limit exceeded")
        time.sleep(15 * 60)
    for tweet_home in home:
        # if tweet_home["user"]["screen_name"] == globals.user:
        put_like(bot, tweet_home)
        likes_count += 1
        time.sleep(2)

    logging.info("Sleeping for 5 minutes.")
    time.sleep(5 * 60)
