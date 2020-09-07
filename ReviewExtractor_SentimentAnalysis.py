# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:37:45 2020

@author: rosha
"""
import urllib, json
from urllib.request import urlopen, Request
import csv

headers={'User-Agent': 'Mozilla/5.0'}
url='https://api.hellopeter.com/consumer/business/discovery-insure/reviews?'
content=[]
for page in range(2, 1685):
    url1=url+ 'page=' + str(page)
    req=Request(url=url1,headers=headers)
    json_url = urlopen(req)
    data = json.loads(json_url.read())
    #print(data)
    content.append(data)

#print(content)

a=(content[0]['data'])
b=a[0]
b['review_content']
r=[]


for i in range(len(content)):
    a=content[i]['data']
    for j in range (len(a)):
        
        customer_info = {
                'Name': a[j]['author'],
                'Title': a[j]['review_title'],
                'Rating': a[j]['review_rating'],
                'Message': a[j]['review_content'],
                'Date':a[j]['created_at']
                    }
        r.append(customer_info)

toCSV = r
with open('Reviews_Dis.csv', 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file, 
                        fieldnames=toCSV[0].keys(),
                       
                       )
    fc.writeheader()
    fc.writerows(toCSV)
        
        
        
