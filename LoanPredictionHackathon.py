# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:50:56 2020

@author: rosha
"""

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression

dataset = pd.read_csv('Train.csv')
X_train = dataset.iloc[:, :-1].values
y_train = dataset.iloc[:, -1].values

X_test=pd.read_csv('Test.csv')


ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0,1,3,4,10])], remainder='passthrough')
X_train = np.array(ct.fit_transform(X_train))
print(X_train)
X_test=np.array(ct.fit_transform(X_test))


classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)