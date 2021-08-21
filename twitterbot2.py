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
import input
import version
import sys
import db
import datetime


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


def retweet_tweet(t, status):
    # Retweet a status
    if not status["retweeted"]:
        logging.info("Retweeted a tweet by {}".format(status["user"]["screen_name"]))
        t.statuses.retweet._id(_id=status["id"])


def search(t, term):
    # Search for the latest tweets about <term>
    return t.search.tweets(q=term)


def create_bot():
    """
    This function returns the authenticated Bot object.
    """
    secretss = secrets.read_secrets()

    if secretss["access_token"] is None or secretss["access_token_secret"] is None:
        logging.error("You must modify properly the config.yaml file.")
        sys.exit(1)

    bot = auth(
        secretss["access_token"],
        secretss["access_token_secret"],
        secretss["api_key"],
        secretss["api_secret_key"],
    )
    return bot


def crawl_timeline(bot):
    """
    This is the handler of the -t or --timeline option.
    """
    tweet_count = 0
    likes_count = 0
    retweet_count = 0

    # check if there are values of today.
    conn = db.conn_db()
    username = globals.bot_user
    values = db.today_stats(conn, username)
    today = datetime.datetime.today().strftime("%Y-%m-%d")

    # if there aren't data, creates a record in the statistics table
    if values is None:
        db.create_stat(conn, (username, today, 0, 0, 0))
    # otherwise retrieves the values
    else:
        (
            username,
            today,
            tweet_count,
            likes_count,
            retweet_count,
        ) = values

    while True:

        logging.info("Tweet count: " + str(tweet_count))
        logging.info("Likes count: " + str(likes_count))
        logging.info("Retweets count: " + str(retweet_count))

        home = get_home(bot)
        if home is not None:
            tweet_count += len(home)
        else:
            logging.warning("Rate limit exceeded")
            time.sleep(15 * 60)
        for tweet_home in home:
            if tweet_home["user"]["screen_name"] != globals.bot_user:
                put_like(bot, tweet_home)
                likes_count += 1
                retweet_tweet(bot, tweet_home)
                retweet_count += 1
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
            if tweet_home["user"]["screen_name"] != globals.bot_user:
                put_like(bot, tweet_home)
                likes_count += 1
                retweet_tweet(bot, tweet_home)
                retweet_count += 1
                time.sleep(2)

        # update the values in the database
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        values = db.today_stats(conn, username)
        # if there aren't data, creates a record in the statistics table
        if values is None:
            db.create_stat(conn, (username, today, 0, 0, 0))
            tweet_count = 0
            likes_count = 0
            retweet_count = 0
        # otherwise update the values
        else:
            db.update_stat(
                conn, (username, today, tweet_count, likes_count, retweet_count)
            )
        logging.info("Database updated.")
        logging.info("Sleeping for 15 minutes.")
        time.sleep(15 * 60)


def main():
    """
    Main function
    """

    logging.basicConfig(
        encoding="utf-8", level=logging.DEBUG, format="%(asctime)s %(message)s"
    )

    args = input.get_args()

    banner.print_banner()

    # -- VERSION --
    if args.version:
        version.print_version()

    # -- TIMELINE --
    if args.timeline:
        bot = create_bot()
        crawl_timeline(bot)

    # -- KEYWORD --
    if args.keyword:
        bot = create_bot()
        ts = search(bot, args.keyword)
        print(ts)

    # -- STATS --
    if args.stats:
        print("STATISTICS.")


if __name__ == "__main__":
    main()
