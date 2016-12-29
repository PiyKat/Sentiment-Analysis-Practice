#! python3

#### Builing a text classifier

import zipfile
import pandas as pd
import numpy as np
import pickle
import nltk
import sys

sys.path.append("C:\Python34\Scripts\Mike AI Job\Tweepy")

import text_preprocessing
from text_preprocessing import tokenise,preprocess,remove_stopwords

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

#training_data = 



