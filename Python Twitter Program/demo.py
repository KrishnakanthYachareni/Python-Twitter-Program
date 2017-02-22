import ORL
import time
from twitter import *

while True:
    d=ORL.twitterOpen()
    twitter_stream = TwitterStream(auth=d)
    iterator = twitter_stream.statuses.sample()
    for tweet in iterator:
        print(tweet)
