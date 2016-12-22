pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive')]

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative')]

tweets = []

for (words,sentiment) in pos_tweets + neg_tweets:
    filtered_words = [e.lower() for e in words.split() if len(e)>=3]
    tweets.append((filtered_words,sentiment))

#print(tweets)

test_tweets = [
    (['feel', 'happy', 'this', 'morning'], 'positive'),
    (['larry', 'friend'], 'positive'),
    (['not', 'like', 'that', 'man'], 'negative'),
    (['house', 'not', 'great'], 'negative'),
    (['your', 'song', 'annoying'], 'negative')]

import nltk

def get_words(tweet_list):
    words_list = []
    for (words,sentiment) in tweet_list :
        words_list.extend(words)
    
    return words_list

def get_word_features(word_list):
    word_freq = nltk.FreqDist(word_list)
    #print(word_freq.most_common())
    
    word_features = word_freq.keys()
    return word_features

words_features = get_word_features(get_words(tweets))

def features_extractor(document):
    
    features = {}
    for words in words_features:
        features['contains(%s)'%words] = (words in document)

    return features

#feat_dict = features_extractor(['love','this','car'])

#print(feat_dict)

training_set = nltk.classify.apply_features(features_extractor, tweets)
#print(training_set)

classifier = nltk.NaiveBayesClassifier.train(training_set)

tweet_try = 'Love this horrible car'
print(classifier.classify(features_extractor(tweet_try.split())))



    

