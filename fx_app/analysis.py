__author__ = 'gregorylevin'

import requests
import re

def analysis(tweet_list):

    #links to NLP sentiment analysis at http://text-processing.com/demo/sentiment/
    url = 'http://text-processing.com/api/sentiment/'
    payload = {'text':tweet_list}
    response = requests.post(url, data=payload)
    return_string = response.content
    numbers = re.findall('\d+(\.\d{1,5})', return_string)
    neg_int = float(numbers[0])
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