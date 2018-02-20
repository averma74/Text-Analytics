import pandas as pd
import operator
import re
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize.casual import _replace_html_entities

import csv

df = pd.read_csv('symantec_tweets.csv', encoding="ISO-8859-1")  # Reading the Twitter Corpus file

df.columns = ["A", "B", "C"]

freqDict = {}

# Start of helper functions.

# Part of speech finder
pos = lambda tokens: pos_tag(tokens)

# Lemmatizer
lemmatize = lambda posTokens: [processPosTagsAndLemmatize(*wordPos) for wordPos in posTokens]


# Returns lemmatization based on PoS
def processPosTagsAndLemmatize(word, pos):
    return lemma.lemmatize(word, treebankToWordnetPOS(pos))


# Replaces unicode
def unicodeReplacement(tweet):
    return _replace_html_entities(tweet)


# Helper function for PoS Tagging
def treebankToWordnetPOS(treebankPosTag):
    return {'J': wordnet.ADJ,
            'V': wordnet.VERB,
            'N': wordnet.NOUN,
            'R': wordnet.ADV}.get(treebankPosTag[0], wordnet.NOUN)


# Declares Lemmatizer
lemma = WordNetLemmatizer()


# End of helper functions

def dictionary(keyword):
    wordCount = 0
    for each in df["C"]:
        if keyword in each.lower():
            wordCount = wordCount + 1
            text = each.lower()  # Makes each Tweet lowercase
            text = unicodeReplacement(text)  # Removes unicode
            text = re.sub(r"http\S+", "", text)  # Removes links
            text = re.sub(r'[0-9]+', '', text)  # Removes numbers
            text = re.sub(r'@(\w)+', '', text)  # Removes Twitter usernames
            text = re.sub(r'\W*\b\w{1,3}\b', '', text)  # Removes single letters
            text = re.sub(r"rt", "", text)  # Removes "rt"
            text = re.sub(r"via", "", text)  # Removes "via"
            text = re.sub(r"&", "", text)  # Removes "&"
            text = re.sub(r"icymi", "", text)  # Removes "ICYMI"

            text = ' '.join(
                [word for word in text.split() if word not in stopwords.words("english")])  # Removes stop words

            tokens = word_tokenize(text)  # Tokenizes the tweets

            tagged = pos(tokens)  # Grabs part of speech

            tagged = lemmatize(tagged)  # Lemmatizes
            tagged = pos(tagged)  # Grabs part of speech again because it is removed in lemmatization

            for word in tagged:
                if word[1] in (
                "NN", "NNS", "NNP", "NNPS", "JJ", "JJR", "JJS"):  # Checks if the word is a noun or adjective
                    if word[0] not in freqDict:  # If word is not already in the frequency list, add it
                        freqDict[word[0]] = 0
                    freqDict[word[0]] += 1  # Once word is in the frequency list, increase its frequency

    sorted_freqDict = sorted(freqDict.items(), key=operator.itemgetter(1))  # Sorts the dictionary by frequency
    sorted_freqDict.reverse()  # Reverses the order

    print("\nWord Count = " + str(wordCount) + "\n")  # Prints total frequency of search word
    # print(sorted_freqDict)

    for word in sorted_freqDict:
        print(word)  # Prints each word and frequency

    # The following lines print the dictionary to a CSV file and are optional
    with open('%sWordCloud.csv' % keyword.lstrip(), 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in sorted_freqDict:
            writer.writerow([key, value])


# The lines to run the code
keyword = input("Enter keyword to be searched: \n")
dictionary(" " + keyword)


