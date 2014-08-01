from django.conf import settings
from django.shortcuts import render
import tweepy
from tweepy import OAuthHandler
import requests
import re

def home(request):
    return render(request, 'home.html')

def tweets(request):

    country = request.POST['country']
    # Good job mvoing your key and secret into settings
    auth = OAuthHandler(settings.CKEY, settings.CSECRET)
    auth.set_access_token(settings.ATOKEN,settings.ASECRET)
    api = tweepy.API(auth)
    #twitterStream = Stream(auth, listener())

    #prints twitter results on page
    tweet_list = []
    search_results = api.search(q=country, count=10000, lang="en")
    for tweet in search_results:
        # print statements should only be for debugging, and should be removed
        print tweet.text
        tweet_list.append(unicode(tweet.text))
    analysis_results = analysis(tweet_list)
    data = {'content': tweet_list, 'analysis_results': analysis_results}
    return render(request, "tweets.html", data)

# This should NOT live in your views file. Only views go here. This code should live elsewhere.
def analysis(tweet_list):

    #links to NLP sentiment analysis at http://text-processing.com/demo/sentiment/
    url = 'http://text-processing.com/api/sentiment/'
    payload = {'text':tweet_list}
    response = requests.post(url, data=payload)
    return_string = response.content
    # Instead of taking JSON results in as a string and then using a regex, you could have made this request w/
    # AJAX. Your JS file would have received the JSON response, and it would be able to parse through it 'normally'
    # e.g., as a dictionary / JS object
    numbers = re.findall('\d+(\.\d{1,5})', return_string)

    neg_int = float(numbers[0])
    # neutral_int = float(numbers[1])
    pos_int = float(numbers[2])

    # What is this if-statement for? Doesn't the API tell you Positive or Negative?
    if pos_int > neg_int:
        label = "POSITIVE"
    else:
        label = "NEGATIVE"

    neg_int = str(int(neg_int*100)) + "%"
    # neutral_int = str(int(neutral_int*100)) + "%"
    pos_int = str(int(pos_int*100)) + "%"
    analysis_results = {'neg_int':neg_int,'label':label, 'pos_int':pos_int}

    return analysis_results

