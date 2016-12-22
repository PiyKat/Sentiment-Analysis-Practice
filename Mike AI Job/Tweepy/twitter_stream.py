import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import string
import nltk
from nltk.corpus import stopwords

consumer_key = '0igxj5V7OsOjNSdzE4R95QWAZ'
consumer_secret = 'LGIDXC8SaVfCKmx2SeNch24SJtEfFDbVgcZOkdBum6gOj3S0UM'
access_token = '810725764329046016-MB96HrY7mp2aJLpHJ6zDTI2ETjBk2aA'
access_secret = 'hl9XmN1QqPSih0a69skE8mvrm0e38GWEpXrnvbWB3HeIY'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)


########### Streaming Section to collect data as it comes ##############

class MyListener(StreamListener):

    def __init__(self):
        super(MyListener,self).__init__()
        self.num_tweets = 0
        
    def on_data(self,data):
        try:
            with open('python_new.json','a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error!")

        return True

    def on_error(self,status):
        print(status)
        return True


user_input = input("Enter your favourite hashtags : ")
#user_input_list = [a for a in user_input.split()]
twitter_stream = Stream(auth,MyListener())
twitter_stream.filter(track = [user_input])


###################### Text Preprocessing ###################

##import re
## 
##emoticons_str = r"""
##    (?:
##        [:=;] # Eyes
##        [oO\-]? # Nose (optional)
##        [D\)\]\(\]/\\OpP] # Mouth
##    )"""
## 
##regex_str = [
##    emoticons_str,
##    r'<[^>]+>', # HTML tags
##    r'(?:@[\w_]+)', # @-mentions
##    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
##    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
## 
##    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
##    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
##    r'(?:[\w_]+)', # other words
##    r'(?:\S)' # anything else
##]
##    
##tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
##emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
## 
##def tokenize(s):
##    return tokens_re.findall(s)
## 
##def preprocess(s, lowercase=False):
##    tokens = tokenize(s)
##    if lowercase:
##
##        # tokens = [token for token in tokens if len(token)>=2]
##        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
##        
##    return tokens
##
##def remove_stopwords(s):
##
##    punctuation = list(string.punctuation)
##    stop = stopwords.words('english') + punctuation + ['rt','via']
##    terms = [term for term in s if term not in stop]
##    return terms
##
##tokens_list = []
##with open('python_new.json','r') as f:
##    for line in f:
##        tweet = json.loads(line)
##        next(f)
##        tokens = remove_stopwords(preprocess(tweet['text']))
##        tokens_list.extend(tokens)
##        
##print(tokens_list)
##        
############## Term Frequencies ##############
##
##word_freq = nltk.FreqDist(tokens_list)
##print(word_freq.most_common())
##
##from nltk import bigrams
##terms_bigram = list(bigrams(tokens_list))
##
##bigram_term_frequency = nltk.FreqDist(terms_bigram)
##print(bigram_term_frequency.most_common(5))


