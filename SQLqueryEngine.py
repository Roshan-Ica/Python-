# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:44:06 2020

@author: rosha
"""

import sqlite3
from sqlalchemy import create_engine
import pandas as pd

df = pd.read_excel("Sample - Superstore.xls")

engine=create_engine('sqlite://', echo=False)

df.to_sql('Store',engine,if_exists='replace', index=False)

results=engine.execute("Select * from Store where profit < 0 & Category='Furniture'")

final=pd.DataFrame(results,columns=df.columns)

output="output.xlsx"

final.to_excel(output, index=False)