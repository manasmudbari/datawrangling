# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 11:02:42 2016

@author: manasmudbari
"""

import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]
    
def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()
    
    for abbv in states:
        #print(abbv)
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken="Auth_key_here")
        df.rename(columns={'Value':str(abbv)}, inplace=True)
        df[abbv] = (df[abbv]-df[abbv][0])/df[abbv][0]*100.0
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
            
    print(main_df.head())
    
    pickle_out = open('fiddy_states3.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()
    
def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken="Auth_key_here")
    df["Value"] = (df["Value"] - df["Value"][0])/df["Value"][0]*100.0
    return df    
    
#fig = plt.figure()
#ax1 = plt.subplot2grid((1,1),(0,0))
#grab_initial_state_data()

HPI_data=pd.read_pickle('fiddy_states3.pickle')
#benchmark = HPI_Benchmark()
#
#HPI_data.plot(ax = ax1)
#benchmark.plot(ax = ax1, color='k', linewidth=10)
#plt.legend().remove()
#plt.show()

HPI_State_Correlation = HPI_data.corr()
print(HPI_State_Correlation)

print(HPI_State_Correlation.describe())