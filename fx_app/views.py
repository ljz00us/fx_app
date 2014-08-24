from django.conf import settings
from django.shortcuts import render
import tweepy
from tweepy import OAuthHandler

from fx_app.analysis import analysis


def home(request):
    return render(request, 'home.html')

def tweets(request):

    #makes POST request
    country = request.POST['country']
    auth = OAuthHandler(settings.CKEY, settings.CSECRET)
    auth.set_access_token(settings.ATOKEN,settings.ASECRET)

    #sends information to TWEEPY
    api = tweepy.API(auth)

    #prints twitter results on page
    tweet_list = []
    search_results = api.search(q=country, count=10000, lang="en")
    for tweet in search_results:
        tweet_list.append(unicode(tweet.text))

    #conducts natural language processing analysis
    analysis_results = analysis(tweet_list)
    data = {'content': tweet_list, 'analysis_results': analysis_results}

    return render(request, "tweets.html", data)



