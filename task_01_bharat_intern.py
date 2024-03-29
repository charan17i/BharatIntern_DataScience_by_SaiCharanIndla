# -*- coding: utf-8 -*-
"""TASK_01_Bharat_intern.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u6pHESnVH-9iJ9ODllYWgMkgLjVqTCDA

Task-1: SMS Classifier

Author: Sai Charan Indla

Domain: Data Science

Aim: Develop a text classification model to
classify SMS as either spam or non-spam
using data science techniques in Python

Import Necessary Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/content/spam.csv",encoding='latin-1')

df.head()

df.tail

df.shape

df.info()

df.describe()

df.isnull().any()

df.isnull().sum()

df.mean()

df.head(5)

df.value_counts()

import nltk

nltk.download('punkt')

nltk.download('stopwords')

nltk.download('wordnet')

message=df.iloc[:,[1]]['v2']

message

label=df.iloc[:,[0]]['v1']

label

"""Label Encoding"""

from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()

label=le.fit_transform(label)

label

le.classes_

import re
from nltk.corpus import stopwords

len(set(stopwords.words('english')))

from nltk.stem import PorterStemmer,WordNetLemmatizer

lemma=WordNetLemmatizer()

from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.tokenize import word_tokenize

sentences=[]
for sen in message:
  senti=re.sub('[^A-Za-z]',' ',sen)
  senti=senti.lower()
  words=word_tokenize(senti)
  word=[lemma.lemmatize(i) for i in words if i not in stopwords.words('english')]
  senti=' '.join(word)
  sentences.append(senti)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf=TfidfVectorizer(max_features=5000)

features=tfidf.fit_transform(sentences)

features=features.toarray()

features

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(sentences)

len(tfidf.get_feature_names_out())

tfidf.get_feature_names_out()

from sklearn.model_selection import train_test_split

feature_train,feature_test,label_train,label_test=train_test_split(features,label,test_size=0.2,random_state=7)

"""Naive Bayies
     
"""

from sklearn.naive_bayes import MultinomialNB

model=MultinomialNB()
model.fit(feature_train,label_train)

label_pred=model.predict(feature_test)

label_pred

label_test

"""Model Evaluation"""

import sklearn.metrics as m

m.accuracy_score(label_test,label_pred)

print(m.classification_report(label_test,label_pred))

print(m.confusion_matrix(label_test,label_pred))