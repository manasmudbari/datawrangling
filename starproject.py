# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 18:19:26 2016

@author: manasmudbari
"""

##----Importing Libraries
import pandas as pd
import numpy as np
import pickle
from urllib2 import Request, urlopen
import json

##----Reading JSON from Github API (currently commented our)
#starGaze = pd.read_json('https://api.github.com/repos/realm/jazzy/stargazers')

##----Reshaping the DataFrame into a matrix
#user_str = starGaze['login'].as_matrix()

##----Searilizing and storing the API data locally
user_out = open('user.pickle','wb')
pickle.dump(user_str, user_out)
user_out.close()

##----Opening locally stored searilized
read_user = pd.read_pickle('user.pickle')

##----Initializing column name for new user DataFrame
columns = ['Name', 'Github Handle', 'Email', 'Company', 'Location']

##----Initializing empty placeholder list
profile_list = []

##----Grabbing stargazer user profile
for i in range(len(read_user)):
    user_html = 'https://api.github.com/users/'+read_user[i]
    request = Request(user_html, headers=hdr)
    response = urlopen(request)
    user_read = response.read()
    user = json.loads(user_read)
    ##----Creating a list of specific values from Github user profile
    temp_list = str(user['name']), str(user['login']), str(user['email']), str(user['company']), str(user['location'])
    ##----concatenating the list to placeholder list
    profile_list.append(temp_list)

##----converting list of lists to DataFrame    
user_profile = pd.DataFrame(profile_list, columns=columns)

##----Exporting to CSV
user_profile.to_csv('example.csv')

#print(user_profile)