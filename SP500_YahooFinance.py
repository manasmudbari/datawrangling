# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 21:47:03 2016

@author: manasmudbari
"""

import pandas as pd
from pandas import DataFrame

import datetime
import pandas.io.data

sp500 = pd.io.data.get_data_yahoo('%5EGSPC', 
                                 start = datetime.datetime(2010, 10, 1), 
                       end = datetime.datetime(2016, 6,1))
                        
sp500.to_csv('sp500_ohlc.csv')

#df = pd.read_csv('sp500_ohlc.csv', index_col = "Date", parse_dates=True)

#print df.head()