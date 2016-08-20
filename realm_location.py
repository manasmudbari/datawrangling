# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:21:42 2016

@author: manasmudbari
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
import sys
from mpl_toolkits.basemap import Basemap

##This piece of code handles the ascii data
reload(sys)
sys.setdefaultencoding('utf-8')

##Initiating basemap
m = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,
        llcrnrlon=-180,urcrnrlon=180,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='#b4ddb4',lake_color='aqua')
m.drawmapboundary()
m.drawcountries()
m.drawstates()

#This code reads our exported CSV file from previous script
df = pd.read_csv('realm.csv')

##Grouping by user's location
new_df = df.groupby('Location')
location_count = new_df['Location'].count()



## This code converts user's location info into list for analysis (bar chart)
x1 = pd.Series(df['Location']).unique()
x1.sort()
x1_pos = np.arange(len(x1))
y1 = location_count.as_matrix()
size = [(int(y1[i])*100)/max(y1) for i in range(len(y1))]

## This code converts user's location data to latitude & longitude for plotting on map
lat = []
lon = []

geolocator = Nominatim()

for i in range(len(x1)):
    location = geolocator.geocode(x1[i])
    lat.append(location.latitude)
    lon.append(location.longitude)
    
    
x,y = m(lon,lat)
m.plot(x, y, c='r')
m.scatter(x, y, s=size, c='r', marker='o')

plt.show()