# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:24:11 2020

@author: rosha
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
from io import BytesIO
import xlsxwriter

df = pd.read_excel("Sample - Superstore.xls")
cols = list(set(df["Category"].values))
cols[1]



pivindex=input('index:').split()
pivdata=input('column:').split()

for k in range (len(cols)):
    df1= df[df["Category"]==cols[k]]
    dfpt=pd.pivot_table(df1,index=pivindex,values=pivdata)
    img=dfpt.plot(kind='bar', secondary_y=pivdata[-1], width=0.8, figsize=(12,10),title=cols[k])
    imgdata=BytesIO()
    fig=plt.figure()
    img.figure.savefig(imgdata)
    
    writer=pd.ExcelWriter('{}.xlsx'.format(cols[k]), engine='xlsxwriter')
    dfpt.to_excel(writer,sheet_name=cols[k])
    t=cols[k]
    worksheet =writer.sheets[t]
    worksheet.insert_image('F1','',{'image_data':imgdata})
    writer.save()