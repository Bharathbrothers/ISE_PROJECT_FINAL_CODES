import requests
import json
import csv
import pprint
#import sys
import pandas as pd



data = pd.read_csv('unique_top1000_data_2.csv')
print('no of unique contributors:', data['username'].nunique())
print('no of unique repositories:', data['repo_name'].nunique())
print('average no of contributions:', data['no_of_contributions'].mean())

reponame=[]
#username =[]
noofcont= []

collaborators =[]
contributions =[]
repos =[]
for i in range(0,length):
    url = "https://api.github.com/repos/mozilla/{}/commits?page=1&per_page=1000".format(repolist[i])
    try:
        get_data = requests.get(url,auth = (uname,token),timeout=10).json()
    except ValueError:
        continue
    #print(len(get_data))
    #print(get_data)
    re = repolist[i]
    print(i)
    for r in get_data:
        repos.append(re)
        collaborators.append(r["login"])
        contributions.append(r["contributions"])
        print(r["login"])
        print(r["contributions"])
