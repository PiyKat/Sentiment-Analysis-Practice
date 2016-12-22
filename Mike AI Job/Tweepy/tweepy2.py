import json

##with open('python_new.json','r') as f:
##    line = f.readline() # Read one tweet
##    tweet = json.loads(line) # load line as a dict
##    print(json.dumps(tweet,indent = 1))

import nltk
from nltk.tokenize import word_tokenize

#nltk.download()
tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
#print(word_tokenize(tweet))

import re

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [o0\-]? # Nose
        [D\)\]\(\]/\\OpP] # Month
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE|re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$',re.VERBOSE|re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s,lowercase = False):
    tokens = tokenize(s)
    if lowercase :
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

#print(preprocess(tweet)) 

dump_dict = []

for x in open('python_new.json','r'):
    dump_dict.append(x)

#print(type(dump_dict))


for tweet_dict in dump_dict:
    
    x = json.dumps(dump_dict)
    tweet_data = json.loads(x)
    print(type(tweet))
    #tweet = preprocess(tweet_data)
    #print(tweet["text"])


##for x in dump_dict:
##    tokens = preprocess(dump_dict['text'])
##
##from nltk import FreqDist
##
##def freq_dict(tweet_list):
##
##    passed_list = [word for word in tweet_list if len(word)>=2]
##    print(passed_list)
##    freqDict = FreqDist(passed_list)
##    key = freqDict.keys()
##
##    return freqDict
##
##print(freq_dict(tokens).most_common())
                        
