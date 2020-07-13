# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:45:53 2020

@author: rosha
"""

import tabula
import camelot

#df = read_pdf("Doc.pdf", pages='all', guess = False)

    
#camelot

tables = camelot.read_pdf("1.pdf")
tables

tables.export('1usingcamelot.csv', f='xlsx', compress=True) 


#tabula
tables = tabula.read_pdf("1.pdf", pages = "all")

tabula.convert_into("RR.pdf", "1usingtabula.xlsx", pages = "all")