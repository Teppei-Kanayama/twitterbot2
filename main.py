import tweepy
import pdb
import random
import json

f = open('keys.json', 'r')
keys = json.load(f)

consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

target = "@nekoneko_full"
status = api.user_timeline(target)
tweet_ids = status.ids()
num = random.randint(0, len(tweet_ids) - 1)
tweet_status = api.get_status(tweet_ids[num])
api.update_status(tweet_status.text)
