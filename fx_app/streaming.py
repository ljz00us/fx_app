__author__ = 'gregorylevin'


# taken from Sentdex
# http://sentdex.com/sentiment-analysisbig-data-and-python-tutorials-algorithmic-trading/how-to-use-the-twitter-api-1-1-to-stream-tweets-in-python/

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = '2iGOP4IROImLs1O08wZT6hQF9'
csecret = 'PADFfUk5OZiBTFzCeqmmo28rTWfhGgkIZ2L7J7epgBTkedIRL3'
atoken = '276084536-5A31Kvaev87cpq1pm8panXDOwdJ2TCm4eXkskge0'
asecret = '6uNTgvFUbDkudFNyDO78eSLtaWfSsEzZy67L2A6WPkd1U'

class listener(StreamListener):

    def on_data(self,data):
        print data
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track = [""])


