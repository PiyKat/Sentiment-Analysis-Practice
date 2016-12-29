#! python3

#### Builing a text classifier

import zipfile
import pandas as pd
import numpy as np
import pickle
import nltk
from nltk import FreqDist
import re
import sys
import sklearn


sys.path.append("C:\Python34\Scripts\Mike AI Job\Final")

#import tweepy2
from text_preprocessing import remove_stopwords

#from text_preprocessing import tokenise,preprocess,remove_stopwords

#zipfile_ref = zipfile.ZipFile("trainingandtestdata.zip","r")
#zipfile_ref.extractall()
#zipfile_ref.close()

##tweets_info = pd.read_csv("training.1600000.processed.noemoticon.csv",encoding = "ISO-8859-1",index_col = 1, header = None)
##
##tweets_info.columns = ["Label","Timestamp","Status","User","Text"]
###print(tweets_info)
##
##training_data = open("training_data","wb")
##pickle.dump(tweets_info,training_data)

datastream = open("training_data","rb")
input_df = pickle.load(datastream)

training_df = input_df[["Label","Text"]]

label_new = ["positive","negative","neutral"]

training_df["Label"] = training_df["Label"].map({4:"positive",2:"neutral",0:"negative"})
training_df = training_df.sample(frac = 1)


training_data = training_df.head(200)


#training_data["Lexicon"] = list(map(text_preprocess.tokenize(str(training_data["Text"])),str(training_data["Text"])))
#training_data["Lexicon"] = map(remove_stopwords(training_data["Text"]))

tweet_list = []

tweet_list = [(remove_stopwords(str(x)),sentiment) for x in training_data["Text"] for sentiment in training_data["Label"]]

def get_words(tweet_list):
    words_list = []
    
    for (words,sentiment) in tweet_list:

        words_list.extend(words)

    return words_list

def get_word_features(words_list):

    word_freq = FreqDist(words_list)
    words_features = word_freq.keys()
    return words_features

def feature_extractor(document):

    features = {}
    for words in words_features:
        features['contains(%s)' %words] = (words in document)

    return features

words_features = get_word_features(get_words(tweet_list))

training_set = training_data.values

text_list = list(training_set[:,1])
sentiment_list = list(training_set[:,0])

tweet_list = [(text,sentiment) for text in text_list for sentiment in sentiment_list]
training_set = nltk.classify.apply_features(feature_extractor,tweet_list)

classifier = nltk.NaiveBayesClassifier.train(training_set)

tweet_try = "I'm happy and cheerful!"
print(classifier.classify(feature_extractor(tweet_try.split())))








