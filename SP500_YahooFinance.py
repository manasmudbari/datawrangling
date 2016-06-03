# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 21:47:03 2016

@author: manasmudbari
"""

#import pandas as pd
#from pandas import DataFrame

#import datetime
#import pandas.io.data

#sp500 = pd.io.data.get_data_yahoo('%5EGSPC', 
                                 #start = datetime.datetime(2010, 10, 1), 
                                  
                                  #end = datetime.datetime(2016, 6,1))
                        
#sp500.to_csv('sp500_ohlc.csv')

df = pd.read_csv('sp500_ohlc.csv', index_col = "Date", parse_dates=True)

#print df.head()

#df2 = df['Open']

#print df2.head()


#df3 = df[['Close', 'Open']]

#print df3.head()

#df3.rename(columns={'Close':'CLOSE'}, inplace = True)

#print df3.head()

#df4 = df3[(df3['CLOSE'] > 1400)]

#print df4

df['H-L'] = df['High'] - df.Low #can also do df['Low']

df['100MA'] = pd.rolling_mean(df['Close'], 100) #moving average for firs 100 days

print df[200:210]