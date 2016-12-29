import json
import nltk
from nltk.tokenize import word_tokenize


import re

from text_preprocessing import remove_stopwords

dump_dict = []

for x in open('python_new.json','r'):
    dump_dict.append(x)

#print(type(dump_dict))

tokens_list = []

with open('python_new.json','r') as f:
    for line in f:
            try :
                tweet = json.loads(line)
                #next(f)
                tokens = remove_stopwords(tweet['text'])
                tokens_list.extend(tokens)
                

            except ValueError as e:
                pass
            
        
#print(tokens_list)

##for tweet_dict in dump_dict:
##    
##    x = json.dumps(dump_dict)
##    tweet_data = json.loads(x)
##    #print(type(tweet))
##    tweet = remove_stopwords(tweet_data)
##    print(tweet["text"])


##for x in dump_dict:
##    tokens = preprocess(dump_dict['text'])

from nltk import FreqDist

def freq_dict(tokens_list):

    passed_list = [word for word in tokens_list if len(word)>=2]
    print(passed_list)
    freqDict = FreqDist(passed_list)
    key = freqDict.keys()

    return freqDict

#print(freq_dict(tokens_list).most_common())

########### Visualization #############

import vincent
from collections import Counter

def lang():

    language = []
    count = Counter()
    with open('python_new.json','r') as f:
        for line in f:
            tweet = json.loads(line)
            language.append(tweet["lang"])
            next(f)

        count.update(language)
    
    word_freq = count.most_common(20)
    labels,freq = zip(*word_freq)
    data = {'data' : freq,'x' : labels}
    bar = vincent.Bar(data,iter_idx = 'x')
    bar.to_json('term_freq.json')

def country():

    country = []
    count = Counter()
    with open('python_new.json','r') as f:
        for line in f:
            tweet = json.loads(line)
            country.append(tweet["user"]["location"])
            next(f)
        
        country_freq = count.update(country)

    word_freq = count.most_common(10)
    labels,freq = zip(*word_freq)
    data = {'data' : freq, 'x' :labels}
    bar = vincent.Bar(data,iter_idx = 'x')
    bar.to_json('country_freq.json')

lang()
country()
