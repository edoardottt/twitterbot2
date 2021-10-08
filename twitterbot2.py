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
# This file contains the main function and all
# the main functionalities of twitterbot2.
# There are defined here the functions to execute the
# right actions when the user inputs his/her choices.
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
import stats
import output
import server
import errors

from threading import Thread


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


def followers(t, username):
    """
    Return the number of followers of the user
    with the username provided as input.
    """
    return t.users.lookup(screen_name=username, _timeout=2)[0]["followers_count"]


def put_like(t, status, logger, count):
    # Favorite/like a status
    if not status["favorited"]:
        logger.info("Liked a tweet by {}".format(status["user"]["screen_name"]))
        t.favorites.create(_id=status["id"])
        count += 1
    return count


def retweet_tweet(t, status, logger, count):
    # Retweet a status
    if not status["retweeted"]:
        logger.info("Retweeted a tweet by {}".format(status["user"]["screen_name"]))
        t.statuses.retweet._id(_id=status["id"])
        count += 1
    return count


def search(t, term):
    # Search for the latest tweets about <term>
    return t.search.tweets(q=term)


def create_bot(logger):
    """
    This function returns the authenticated Bot object.
    """
    secretss = secrets.read_secrets()

    if secretss["access_token"] is None or secretss["access_token_secret"] is None:
        logger.error("You must modify properly the config.yaml file.")
        sys.exit(1)

    bot = auth(
        secretss["access_token"],
        secretss["access_token_secret"],
        secretss["api_key"],
        secretss["api_secret_key"],
    )
    return bot


def likes_rt_home(bot, logger, tweet_count, likes_count, retweet_count):
    """
    This function tries to put likes and retweet the tweets in
    the bot timeline.
    """

    try:
        home = get_home(bot)
    except twitter.api.TwitterHTTPError as e:
        errors.error_handler(e)

    if home is not None:
        tweet_count += len(home)

    for tweet_home in home:
        if tweet_home["user"]["screen_name"] != globals.bot_user:

            try:
                likes_count = put_like(bot, tweet_home, logger, likes_count)
            except twitter.api.TwitterHTTPError as e:
                errors.error_handler(e)

            try:
                retweet_count = retweet_tweet(bot, tweet_home, logger, retweet_count)
            except twitter.api.TwitterHTTPError as e:
                errors.error_handler(e)

            time.sleep(2)

    return tweet_count, likes_count, retweet_count


def likes_rt_user(bot, logger, tweet_count, likes_count, retweet_count):
    """
    This function tries to put likes and retweet the tweets in
    the user timeline.
    """
    try:
        home = get_friend_home(bot, globals.user)
    except twitter.api.TwitterHTTPError as e:
        errors.error_handler(e)

    if home is not None:
        tweet_count += len(home)

    for tweet_home in home:
        if tweet_home["user"]["screen_name"] != globals.bot_user:

            try:
                likes_count = put_like(bot, tweet_home, logger, likes_count)
            except twitter.api.TwitterHTTPError as e:
                errors.error_handler(e)

            try:
                retweet_count = retweet_tweet(bot, tweet_home, logger, retweet_count)
            except twitter.api.TwitterHTTPError as e:
                errors.error_handler(e)

            time.sleep(2)

    return tweet_count, likes_count, retweet_count


def crawl_timeline(bot, logger, no_user):
    """
    This is the handle function of the -t or --timeline option.
    """
    tweet_count = 0
    likes_count = 0
    retweet_count = 0
    followers_count = 0

    # check if there are values of today.
    conn = db.conn_db()
    username = globals.bot_user
    values = db.today_stats(conn, username)
    today = datetime.datetime.today().strftime("%Y-%m-%d")

    # if there aren't data, creates a record in the statistics table
    if values is None:
        db.create_stat(conn, (username, today, 0, 0, 0, 0))
    # otherwise retrieves the values
    else:
        (
            username,
            today,
            tweet_count,
            likes_count,
            retweet_count,
            followers_count,
        ) = values

    while True:

        logger.info("Today tweets count: " + str(tweet_count))
        logger.info("Today likes count: " + str(likes_count))
        logger.info("Today retweets count: " + str(retweet_count))
        logger.info("Followers count: " + str(followers_count))

        tweet_count, likes_count, retweet_count = likes_rt_home(
            bot, logger, tweet_count, likes_count, retweet_count
        )

        logger.info("Sleeping for one minute.")
        time.sleep(60)

        if no_user:
            tweet_count, likes_count, retweet_count = likes_rt_home(
                bot, logger, tweet_count, likes_count, retweet_count
            )
        else:
            tweet_count, likes_count, retweet_count = likes_rt_user(
                bot, logger, tweet_count, likes_count, retweet_count
            )

        # update the values in the database
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        values = db.today_stats(conn, username)

        # retrieve the up-to-date followers count
        try:
            followers_count = followers(bot, globals.bot_user)
        except twitter.api.TwitterHTTPError as e:
            errors.error_handler(e)

        # if there aren't data, creates a record in the statistics table
        if values is None:
            db.create_stat(conn, (username, today, 0, 0, 0, 0))
            tweet_count = 0
            likes_count = 0
            retweet_count = 0
        # otherwise update the values
        else:
            db.update_stat(
                conn,
                (
                    tweet_count,
                    likes_count,
                    retweet_count,
                    followers_count,
                    username,
                    today,
                ),
            )
        logger.info("Database updated.")

        # check if the bot reached the monthly tweet cap
        if db.month_stats(conn, username)[2] > globals.month_tweet_cap:
            logger.critical("Monthly tweet cap reached.")
            logger.critical("Exiting.")
            sys.exit()

        # check if the bot reached the daily tweet cap
        if retweet_count + 40 > globals.daily_tweet_cap:
            logger.warning("Daily tweet cap reached.")
            logger.info("Sleeping for 2 hours.")
            time.sleep(2 * 60 * 60)
        else:
            logger.info("Sleeping for 15 minutes.")
            time.sleep(15 * 60)


def likes_rt_search(bot, logger, keyword, tweet_count, likes_count, retweet_count):
    """
    This function tries to put likes and retweet the tweets searched by term.
    """
    ts = search(bot, keyword)
    statuses = ts["statuses"]

    if statuses is not None:
        tweet_count += len(statuses)
    else:
        logger.warning("Rate limit exceeded")
        time.sleep(15 * 60)
    for tweet_ts in statuses:
        if tweet_ts["user"]["screen_name"] != globals.bot_user:
            likes_count = put_like(bot, tweet_ts, logger, likes_count)
            retweet_count = retweet_tweet(bot, tweet_ts, logger, retweet_count)
            time.sleep(2)
    return tweet_count, likes_count, retweet_count


def crawl_keyword(bot, logger, keyword, no_user):
    """
    This is the handle function of the -k or --keyword option.
    """
    tweet_count = 0
    likes_count = 0
    retweet_count = 0
    followers_count = 0

    # check if there are values of today.
    conn = db.conn_db()
    username = globals.bot_user
    values = db.today_stats(conn, username)
    today = datetime.datetime.today().strftime("%Y-%m-%d")

    # if there aren't data, creates a record in the statistics table
    if values is None:
        db.create_stat(conn, (username, today, 0, 0, 0, 0))
    # otherwise retrieves the values
    else:
        (
            username,
            today,
            tweet_count,
            likes_count,
            retweet_count,
            followers_count,
        ) = values

    while True:

        try:
            logger.info("Today tweets count: " + str(tweet_count))
            logger.info("Today likes count: " + str(likes_count))
            logger.info("Today retweets count: " + str(retweet_count))
            logger.info("Followers count: " + str(followers_count))

            tweet_count, likes_count, retweet_count = likes_rt_search(
                bot, logger, keyword, tweet_count, likes_count, retweet_count
            )

            logger.info("Sleeping for one minute.")
            time.sleep(60)

            if no_user:
                tweet_count, likes_count, retweet_count = likes_rt_search(
                    bot, logger, keyword, tweet_count, likes_count, retweet_count
                )
            else:
                tweet_count, likes_count, retweet_count = likes_rt_user(
                    bot, logger, tweet_count, likes_count, retweet_count
                )

            # update the values in the database
            today = datetime.datetime.today().strftime("%Y-%m-%d")
            values = db.today_stats(conn, username)
            # retrieve the up-to-date followers count
            followers_count = followers(bot, globals.bot_user)
            # if there aren't data, creates a record in the statistics table
            if values is None:
                db.create_stat(conn, (username, today, 0, 0, 0, 0))
                tweet_count = 0
                likes_count = 0
                retweet_count = 0
            # otherwise update the values
            else:
                db.update_stat(
                    conn,
                    (
                        tweet_count,
                        likes_count,
                        retweet_count,
                        followers_count,
                        username,
                        today,
                    ),
                )
            logger.info("Database updated.")

            # check if the bot reached the monthly tweet cap
            if db.month_stats(conn, username)[2] > globals.month_tweet_cap:
                logger.critical("Monthly tweet cap reached.")
                logger.critical("Exiting.")
                sys.exit()

            # check if the bot reached the daily tweet cap
            if retweet_count + 40 > globals.daily_tweet_cap:
                logger.warning("Daily tweet cap reached.")
                logger.info("Sleeping for 6 hours.")
                time.sleep(6 * 60 * 60)
            else:
                logger.info("Sleeping for 15 minutes.")
                time.sleep(15 * 60)
            logger.info("Sleeping for 15 minutes.")
            time.sleep(15 * 60)
        except twitter.api.TwitterHTTPError as e:

            if tweet_count != 0:
                db.update_stat(
                    conn,
                    (
                        tweet_count,
                        likes_count,
                        retweet_count,
                        followers_count,
                        username,
                        today,
                    ),
                )
            logger.info("Database updated.")
            logger.error(str(e.e) + " on " + e.uri)
            logger.info("Sleeping for one hour.")
            time.sleep(60 * 60)


def main():
    """
    Main function
    """
    logger = logging.getLogger(__name__)

    logging.basicConfig(
        encoding="utf-8",
        level=logging.INFO,
        filename="twitterbot2.log",
        filemode="a",
        format=globals.bot_user + ": %(levelname)s:%(asctime)s | %(message)s",
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s:%(asctime)s | %(message)s")
    console.setFormatter(formatter)
    logger.addHandler(console)

    args = input.get_args()

    banner.print_banner()

    at_least_one_option = False

    # -- VERSION --
    if args.version:
        at_least_one_option = True
        version.print_version()

    # -- TIMELINE --
    if args.timeline:
        at_least_one_option = True
        bot = create_bot(logger)
        t1 = Thread(
            target=crawl_timeline,
            args=(
                bot,
                logger,
                args.no_user,
            ),
        )
        t2 = Thread(target=server.app.run, kwargs={"host": "0.0.0.0"})
        t1.start()
        t2.start()

    # -- KEYWORD --
    if args.keyword:
        at_least_one_option = True
        bot = create_bot(logger)
        t1 = Thread(
            target=crawl_keyword,
            args=(
                bot,
                logger,
                args.keyword,
                args.no_user,
            ),
        )
        t2 = Thread(target=server.app.run, kwargs={"host": "0.0.0.0"})
        t1.start()
        t2.start()

    # -- STATS --
    if args.stats:
        at_least_one_option = True
        stats.check_stat(args.stats)

    # -- CSV OUTPUT --
    if args.output_csv:
        at_least_one_option = True
        output.output_csv(args.output_csv)

    # -- JSON OUTPUT --
    if args.output_json:
        at_least_one_option = True
        output.output_json(args.output_json)

    # -- HTML OUTPUT --
    if args.output_html:
        at_least_one_option = True
        output.output_html(args.output_html)

    if not at_least_one_option:
        version.print_version()


if __name__ == "__main__":
    main()
