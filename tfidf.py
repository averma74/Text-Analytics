# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 23:24:02 2018

@author: adite
"""
import pandas as pd

#Extracting the Group A csv 
df1 = pd.read_csv('Type2_MasterA_tweets_Thesaurus50.csv', encoding="ISO-8859-1")
df1.columns = ["A", "B"]
bowB = df1["A"] #taking only the words

#Extracting the Group B csv 
df2 = pd.read_csv('Type2_MasterB_tweets_Thesaurus50.csv', encoding="ISO-8859-1")
df2.columns = ["A", "B"]
bowA = df2["A"] #taking only the words

wordSet= set(bowA).union(set(bowB))

wordDictA = dict.fromkeys(wordSet, 0)
wordDictB = dict.fromkeys(wordSet, 0)

for word in bowA:
    wordDictA[word]+=1
    
for word in bowB:
    wordDictB[word]+=1
    
pd.DataFrame([wordDictA, wordDictB])

#module to compute TF
def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)
    return tfDict

tfBowA = computeTF(wordDictA, bowA)
tfBowB = computeTF(wordDictB, bowB)

#module to compute IDF
def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(),0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] +=1
    
    for word, val in idfDict.items():
        idfDict[word]= math.log(N / float(val))
        
    return idfDict

idfs = computeIDF([wordDictA, wordDictB])

#module to compute TFIDF
def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val * idfs[word]
    return tfidf

tfidfBowA = computeTFIDF(tfBowA, idfs)
tfidfBowB = computeTFIDF(tfBowB, idfs)

#converting data to dataframe
df = pd.DataFrame([tfidfBowA, tfidfBowB])
df1 = df.T #took transpose

#saving the dataframe as a csv file
df1.to_csv('myDataFrame.csv') 