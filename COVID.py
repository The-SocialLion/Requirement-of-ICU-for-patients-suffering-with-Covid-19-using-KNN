# -*- coding: utf-8 -*-
"""Untitled36.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1csBg8HOy0BStdHp3KBoJc6neg_qxO4Cy
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

dataset=pd.read_csv('covid.csv',nrows=15000)
dataset=dataset.dropna(how='any')
df=dataset.drop(columns=['date_died','id'])
df['intubed'] = df['intubed'].replace([97],0)
df['pregnancy'] = df['pregnancy'].replace([97],0)
df['contact_other_covid'] = df['contact_other_covid'].replace([99],0)
df['icu'] = df['icu'].replace([97],0)
df[['entry_date','date_symptoms']] = df[['entry_date','date_symptoms']].apply(pd.to_datetime) 
df['C'] = (df['date_symptoms'] - df['entry_date']).dt.days
df['Days']=abs(df['C'])
df=df.drop(columns=['date_symptoms','entry_date','C'])
df['Icu']=df['icu']
df=df.drop(columns=['icu'])
df

X=df.iloc[:,:-1].values
y=df.iloc[:,-1].values

y=y.reshape(len(y),1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15, random_state = 0)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 12250, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred)*100)