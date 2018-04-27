# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 18:34:00 2018

@author: adite
"""

import pandas as pd
import numpy as np

#extracting the csv file
doc = pd.read_csv('myDataFrame.csv', encoding="ISO-8859-1")
doc.columns = ["Word", "A", "B"]

#naming the columns
Words = doc["Word"]
GroupA = doc["A"]
GroupB = doc["B"]

#counting the number of total words
WordCount = 0
for each in Words:
    WordCount = WordCount + 1

print("Word Count:" + str(WordCount))    

SimilarityCount = 0

#counting the number of similar words
for i,j in zip (doc["A"], doc["B"]):
    if i == j:
                SimilarityCount = SimilarityCount + 1
   
print("Similarity Count = " + str(SimilarityCount))

#taking percentage
percentage = (SimilarityCount/WordCount)*100
print("Similarity Percentage:")
print(np.around(percentage,decimals=2))
