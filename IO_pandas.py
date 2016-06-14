# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:15:34 2016

@author: manasmudbari
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

df=pd.read_csv('~/Documents/datawrangling/ZILL-Z94609_MLP.csv')

df.set_index('Date', inplace=True)
print(df.head())

df.to_csv('~/Documents/datawrangling/newcsv.csv')

df1 = pd.read_csv('~/Documents/datawrangling/newcsv.csv', index_col=0)



df1.columns = ['Austin_HPI']

print(df1.head())

df.to_csv('~/Documents/datawrangling/noheader.csv', header=False) #no header

df2 = pd.read_csv('~/Documents/datawrangling/noheader.csv', names=['Date','Austin_HPI'])
#putting the header name back with names=['Header1', 'header2', etc.]

print(df2.head())