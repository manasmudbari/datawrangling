# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 00:36:48 2016

@author: manasmudbari
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
import sys

#this piece of code handles the ascii data
reload(sys)
sys.setdefaultencoding('utf-8')

df = pd.read_csv('realm.csv')

##Grouping by location
new_df = df.groupby('Location')

location_count = new_df['Location'].count()

x = pd.Series(df['Location']).unique()
x.sort()
x_pos = np.arange(len(x))

y = location_count.as_matrix()

plt.bar(x_pos, y, align='center', color='#59569e', alpha=0.7, width=0.35)
plt.xticks(x_pos, x)
plt.ylabel('Stargazer Count')
plt.title('Realm repo stargazers count by location')
plt.show()




#geolocator = Nominatim()
#location geolocator.geocode() 