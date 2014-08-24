__author__ = 'gregorylevin'

import requests
import re
from wordnik import *


def analysis(tweet_list):

    #links to NLP sentiment analysis at http://text-processing.com/demo/sentiment/
    url = 'http://text-processing.com/api/sentiment/'
    payload = {'text':tweet_list}
    response = requests.post(url, data=payload)
    return_string = response.content
    numbers = re.findall('\d+(\.\d{1,5})', return_string)
    neg_int = float(numbers[0])

    # "neutral int" is another number returned by the API
    # but is unused for this app
    # neutral_int = float(numbers[1])
    pos_int = float(numbers[2])

    if pos_int > neg_int:
        label = "POSITIVE"
    else:
        label = "NEGATIVE"

    neg_int = str(int(neg_int*100)) + "%"
    # neutral_int = str(int(neutral_int*100)) + "%"
    pos_int = str(int(pos_int*100)) + "%"
    analysis_results = {'neg_int':neg_int,'label':label, 'pos_int':pos_int}

    return analysis_results

# def dictionary():
#
#     apiUrl = 'http://api.wordnik.com/v4'
#     apiKey = 'YOUR API KEY HERE'
#     client = swagger.ApiClient(apiKey, apiUrl)
#
#     wordApi = WordApi.WordApi(client)
#     example = wordApi.getTopExample('irony')
#     dict_data = {'example_text':example.text}
#
#     return dict_data

    # https://github.com/wordnik/wordnik-python
