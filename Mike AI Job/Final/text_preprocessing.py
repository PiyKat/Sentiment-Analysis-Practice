import json
import string
import nltk
from nltk.corpus import stopwords
import re
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
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
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:

        # tokens = [token for token in tokens if len(token)>=2]
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
        
    return tokens

def remove_stopwords(s):

    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['rt','via']
    terms = [term for term in s if term not in stop]
    return terms

tokens_list = []
with open('python_new.json','r') as f:
    for line in f:
        count = 0
        while count < 30:
            try :
                tweet = json.loads(line)
                next(f)
                tokens = remove_stopwords(preprocess(tweet['text']))
                tokens_list.extend(tokens)
                count += 1

            except ValueError as e:
                pass
            
        
#print(tokens_list)
        
############ Term Frequencies ##############

word_freq = nltk.FreqDist(tokens_list)
print(word_freq.most_common())

from nltk import bigrams
terms_bigram = list(bigrams(tokens_list))

#bigram_term_frequency = nltk.FreqDist(terms_bigram)
#print(bigram_term_frequencies.most_common(5))
