# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:32:06 2020

@author: Adrita Choudhury
"""

import pandas
df = pandas.read_csv('CSVfile.csv',index_col="Name")
print(df)
df = pandas.read_csv('CSVfile.csv', index_col='Name', parse_dates=['Hire Date'])
print(df)
df = pandas.read_csv('CSVfile.csv', 
            index_col='Employee', 
            parse_dates=['Hired'], 
            header=0, 
            names=['Employee', 'Hired','Salary', 'Sick Days'])
print(df)