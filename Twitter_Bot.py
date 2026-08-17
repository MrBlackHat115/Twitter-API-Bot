import tweepy
import time

# Replace these with your own Twitter/X API credentials.
# Never share or commit your API keys, secrets, or access tokens.

auth = tweepy.OAuthHandler(
    consumer_key,
    consumer_secret
)

auth.set_access_token(
    access_token,
    access_token_secret
)

api = tweepy.API(auth)

user = api.me()


def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(300)


# Option 1: You can follow back whoever follows you

# for follower in limit_handler(tweepy.Cursor(api.followers).items()):

#     if follower.name == "USERNAME":
#         follower.follow()
#         break


# Option 2: You can search for specific titles that you want to like

# search_string = "Python"

# number_of_tweets = 2

# for tweet in tweepy.Cursor(
#     api.search,
#     search_string
# ).items(number_of_tweets):
#     try:
#         tweet.favorite()
#         print("I liked that tweet!")
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break