# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:38:39 2020

@author: rosha
"""



import csv
import requests

CSV_URL = 'https://query1.finance.yahoo.com/v7/finance/download/RELIANCE.NS?period1=820454400&period2=1593561600&interval=1mo&events=history'


with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    

from pandas import DataFrame
column_names = my_list.pop(0)
df = DataFrame(my_list, columns=column_names)
df.describe

df.to_csv('Reliance.csv')

import pandas as pd
import matplotlib.pyplot as plt
x = df.Date 
y=df.Open
plt.plot(x, y) 
        