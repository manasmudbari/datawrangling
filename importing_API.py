# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 18:53:04 2016

@author: manasmudbari
"""

import matplotlib.pyplot as plt
import numpy as np
import urllib
import datetime as dt
import matplotlib.dates as mdates

#def nasa_sound(type):
#    nasa_url = 'https://api.nasa.gov/planetary/sounds?q='+type+'&api_key=tEKfCUV0r8RY6gPgCBtxewegDw4Jlh1DRDLQYoqd'
#    source_code = urllib.urlopen(nasa_url).read()
#    sound_data = []
#    split_source = source_code.split('\n')
#    print(sound_data)
#nasa_sound('apollo')

#Decoding the data
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):
    
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))
    
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'

    source_code = urllib.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')
    
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line:
                stock_data.append(line)
    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data, delimiter=',', unpack=True, 
                                                          #%Y = full year. 2015
                                                          # %y = partial year 15
                                                          # %m = number month
                                                          # %d = number day
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          # 12-06-2014
                                                          # %m-%d-%Y
                                                          converters={0: bytespdate2num('%Y%m%d')})                   
    
    ax1.plot_date(date, closep, '-', label='Price')
    ax1.plot([],[],linewidth=5, label='loss', color='r', alpha=0.5)
    ax1.plot([],[],linewidth=5, label='gain', color='g', alpha=0.5)    
    ax1.axhline(closep[0], color='k', linewidth=0.5)
    ax1.fill_between(date, closep, closep[0],
                     where=(closep > closep[0]), facecolor='g', alpha=0.5) #alpha determines opacity
    ax1.fill_between(date, closep, closep[0],
                     where=(closep < closep[0]), facecolor='r', alpha=0.5)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)
#    ax1.xaxis.label.set_color('c')
#    ax1.yaxis.label.set_color('r')
    ax1.set_yticks([0,25,50,75])
        
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.18, 
                        right=0.94, top=0.95, wspace=0.2, hspace=0)
    plt.show()
    
graph_data('TWTR')
