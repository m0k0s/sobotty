
# coding: utf-8

# Dependencies
import pandas as pd
import tweepy
import time
import json
import random
from twitter_config import consumer_key, consumer_secret, access_token, access_token_secret




# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret


# Quotes to Tweet
happy_quotes = [
    "Can you see my halo? - Beyonce",
    "You get a car. - Oprah",
    "Hope-y change-y thing. - Sarah Palin",
    "George Bush doesn't care about Black people. - Kanye West",
    "You've got to go to work on Myra's feet. - Martin Lawrence"]




# Create function for tweeting
def HappyItUp():

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet a random quote
    api.update_status(random.choice(happy_quotes))

    # Print success message
    print("Tweeted successfully!")


# Set timer to run every minute
while(True):
    HappyItUp()
    time.sleep(60)

