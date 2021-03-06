# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 18:19:26 2016
@author: manasmudbari

This code pulls stargazers from select Github repo and exports the required 
user information to CSV file

"""

##----Importing Libraries
import pandas as pd
import numpy as np
import pickle
from urllib2 import Request, urlopen
import json
import sys

#this piece of code handles the ascii data
reload(sys)
sys.setdefaultencoding('utf-8')

##----Reading JSON from Github API (currently commented our)

def repoRead(repo_name):
    repo_URL = 'https://api.github.com/repos/realm/'+repo_name+'/stargazers'
    starGaze = pd.read_json(repo_URL)
    ##----Reshaping the DataFrame into a matrix
    user_str = starGaze['login'].as_matrix()
    ##----Searilizing and storing the API data locally
    user_out = open('user.pickle','wb')
    pickle.dump(user_str, user_out)
    user_out.close()

def userProfile():
    ##----Opening locally stored searilized
    read_user = pd.read_pickle('user.pickle')
    ##----Initializing column name for new user DataFrame
    columns = ['Name', 'Github Handle', 'Email', 'Company', 'Location', 'Blog', 'Followers', 'Following']

    ##----Initializing empty placeholder list
    profile_list = []
    ##----Grabbing stargazer user profile
    for i in range(len(read_user)):
        user_html = 'https://api.github.com/users/'+read_user[i]
        request = Request(user_html)
        response = urlopen(request)
        user_read = response.read()
        user = json.loads(user_read)
        ##----Creating a list of specific values from Github user profile
        temp_list = str(user['name']), str(user['login']), str(user['email']), str(user['company']), str(user['location']), str(user['blog']), int(user['followers']), int(user['following'])
        ##----concatenating the list to placeholder list
        profile_list.append(temp_list)
    ##----converting list of lists to DataFrame    
    user_profile = pd.DataFrame(profile_list, columns=columns)
    
    ##----Exporting to CSV
    user_profile.to_csv('realm_new.csv')
    
##Step1: Remove the # sign below to import stargazers from select GitHub repo
#repoRead('jazzy')

##Step2: After running the code above, remove # below and run the following code to export user profile to CSV
#userProfile()