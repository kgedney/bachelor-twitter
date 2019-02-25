#- set working directory
import os
project_root = '/Users/kgedney/Documents/projects/bachelor-twitter'
os.chdir(project_root)

#- install packages
import sys
import json
import tweepy
import numpy as np
import pandas as pd

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# set twitter api credentials
credentials = json.load(open('credentials.json'))

consumer_key    = credentials['consumer_key']
consumer_secret = credentials['consumer_secret']
access_token    = credentials['access_token']
access_secret   = credentials['access_secret']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

# define stream
class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        #print(status.text)
        print(json.dumps(status._json))
        sys.stdout.flush()
        
    def on_error(self, status_code):
        print('Error', file=sys.stderr)
        if status_code == 420:
            return False


if __name__ == "__main__":
    
    # define filters, case does not matter
    track = ['the bachelor', 
         '#thebachelor',
         '#bachelornation',
         '#bachelorabc',
         'colton',
         '#colton',
         '#hometowns',
         'hometowns'
        ]
    
    #track = ['#trump', '#POTUS']
    
    print('collect.py: starting to listen', file=sys.stderr)
    stream_listener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(track=track)

