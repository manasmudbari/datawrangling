# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 00:36:48 2016

@author: manasmudbari
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


##This piece of code handles the ascii data
reload(sys)
sys.setdefaultencoding('utf-8')



#This code reads our exported CSV file from previous script
df = pd.read_csv('realm_new.csv') #-- type the name of your exported CSV here        

def location_plot():
    ##Grouping by user's location
    new_df = df.groupby('Location')
    location_count = new_df['Location'].count()
    ## This code converts user's location info into list for analysis (bar chart)
    x1 = pd.Series(df['Location']).unique()
    x1.sort()
    x1_pos = np.arange(len(x1))
    y1 = location_count.as_matrix()
    
    plt.bar(x1_pos, y1, align='center', color='#59569e', alpha=0.7, width=0.35)
    plt.xticks(x1_pos, x1, rotation=85)
    plt.xlabel('Stargazer\'s Location')
    plt.ylabel('Stargazer Count')
    plt.title('Realm repo stargazers count by location')
    plt.tight_layout()
    plt.show()

def company_plot():
    ##Grouping by user's company
    company_df = df.groupby('Company')
    company_count = company_df['Company'].count()
    
    ## This code converts user's company info into list for analysis (bar chart)
    x2 = pd.Series(df['Company']).unique()
    x2.sort()
    x2_pos = np.arange(len(x2))
    y2 = company_count.as_matrix()
    
    plt.bar(x2_pos, y2, align='center', color='#d34ca3', alpha=0.7, width=0.35)
    plt.xticks(x2_pos, x2, rotation=85)
    plt.xlabel('Stargazer\'s Company')
    plt.ylabel('Stargazer Count')
    plt.title('Realm repo stargazers count by company')
    plt.tight_layout()
    plt.show()


##Remove # from code below to plot stargazers number by company name
#company_plot()

##Remove # from code below to plot stargazers number by location
location_plot()
    