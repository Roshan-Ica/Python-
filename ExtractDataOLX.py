# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:12:49 2020

@author: rosha
"""

import urllib, json
import csv

url = "https://www.olx.in/api/relevance/search?category=84&facet_limit=100&lang=en&location=4059162&location_facet_limit=20&showAllCars=true&user=17169665b6cx1796aae9"
content=[]
for page in range(0,20):
    json_url = urllib.request.urlopen(url+ '&page=' + str(page))
    data = json.loads(json_url.read())
    print(data)
    
    for offer in data['data']:
                items = {
                    'title': offer['title'],
                    'description': offer['description'].replace('\n', ' '),
                    'location': offer['locations_resolved']['COUNTRY_name'] + ', ' +
                                offer['locations_resolved']['ADMIN_LEVEL_1_name'] + ', ' +
                                offer['locations_resolved']['ADMIN_LEVEL_3_name'],
                    'features': offer['main_info'],
                    'date': offer['display_date'],
                    'price': offer['price']['value']['display']
                }
                print(json.dumps(items, indent=2))
                content.append(items)
toCSV = content
with open('cars_ind.csv', 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file, 
                        fieldnames=toCSV[0].keys(),
                       
                       )
    fc.writeheader()
    fc.writerows(toCSV)