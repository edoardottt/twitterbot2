#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#
# This file contains some global values needed by
# twitterbot2 while running.
# You should edit the last two ('user' and 'bot_user') values.
#


# ==== CHANGE THESE VALUES ====

user = "edoardottt2"  # your profile | in my case: https://twitter.com/edoardottt2
bot_user = "ai_testing"  # the bot | in my case: https://twitter.com/ai_testing

# =============================


# API LIMITS (EVERY VALUE per 15 minutes)

api_limits = {
    "tweet_lookup": {
        "description": "Pull detailed, up-to-date information about a specific Tweet or Tweets using an ID.",
        "user_auth": 900,
        "app_auth": 300,
    },
    "recent_search": {
        "description": "Discover public Tweets posted within the last seven days using all \
            available fields and expansions. Tweets will show up in reverse-chronological order.",
        "user_auth": 180,
        "app_auth": 450,
    },
    "recent_tweet_counts": {
        "description": "The Tweet Counts endpoints allows you to programmatically get the \
            data volume of Tweets over the past seven days for a search query",
        "app_auth": 300,
    },
    "user_mention_timeline": {
        "description": "Get Tweets that mention the specified user.",
        "app_auth": 450,
        "user_auth": 180,
    },
    "user_tweet_timeline": {
        "description": "Get Tweets created by the specified user.",
        "app_auth": 1500,
        "user_auth": 900,
    },
    "filtered_stream": {
        "description": "Get all the Tweets in real-time that match the search criteria you've set.",
        "app_auth": 50,
    },
    "sampled_stream": {
        "description": "Get about a 1% random sample of all Tweet data, in real time, through a streaming connection.",
        "app_auth": 50,
    },
    "user_lookup": {
        "description": "Pull detailed, up-to-date information about a single Twitter user or \
            multiple users using an ID or @username.",
        "user_auth": 900,
        "app_auth": 300,
    },
    "follows_lookup": {
        "description": "Get the accounts following (followers) or accounts followed by (following) a specified user.",
        "user_auth": 15,
        "app_auth": 15,
    },
    "manage_follows": {
        "description": "Follow or unfollow a user (target) on behalf of another user (source).",
        "user_auth": 15,
    },
    "manage_blocks": {
        "description": "Block or unblock a user (target) on behalf of another user (source).",
        "user_auth": 50,
    },
    "manage_mutes": {
        "description": "Mute or unmute a user (target) on behalf of another user (source).",
        "user_auth": 50,
    },
    "mutes_lookup": {
        "description": "Get the accounts that a specified user is currently muting.",
        "user_auth": 15,
    },
    "blocks_lookup": {
        "description": "Get the accounts that a specified user is currently blocking.",
        "user_auth": 15,
    },
    "hide_replies": {
        "description": "Programmatically hide or unhide replies to improve the quality of the conversation",
        "user_auth": 50,
    },
    "likes_lookup": {
        "description": "Get the accounts that a specified user is currently blocking.",
        "user_auth": 75,
        "app_auth": 75,
    },
    "manage_likes": {
        "description": "Like or un-like a Tweet on behalf of a user, using the Tweet ID",
        "user_auth": 50,
    },
    "manage_retweets": {
        "description": "Retweet or undo a Retweet on behalf of a user, using the Tweet ID",
        "user_auth": 50,
        "app_auth": 25,
    },
    "retweets_lookup": {
        "description": "Get a list of Twitter users that have retweeted a Tweet.",
        "user_auth": 75,
        "app_auth": 75,
    },
    "batch_compliance": {
        "description": "Keep your datasets in compliance by retrieving compliance status for Tweets and users in bulk.",
        "app_auth": 150,
    },
    "search_spaces": {
        "description": "Search Spaces based on keywords, and filter results by status.",
        "user_auth": 150,
        "app_auth": 150,
    },
    "spaces_lookup": {
        "description": "Detailed, up-to-date information about one or more Space you can \
            lookup by ID or based on people you follow.",
        "user_auth": 300,
        "app_auth": 300,
    },
}

month_tweet_cap = 500000
daily_tweet_cap = 2400
quarter_hour_cap = 300
