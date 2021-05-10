import requests
import json
import csv
import pprint
import sys
#import pandas as pd

username = "mozilla"

repolist = []

uname = "Bharathbrothers"
token = "6eb9643ba09cea0ca71abcfd88b81aea3f5a65d1"


for i in range(1,21):
    url = "https://api.github.com/orgs/"+username+"/repos?page={}&per_page=100".format(i)
    get_data = requests.get(url,auth = (uname,token)).json()
    print(len(get_data))
    for r in get_data:
        repolist.append(r["name"])


print(len(repolist))
#print(repolist)

with open('repositorieslist.csv','w',newline='',encoding="utf-8") as wfile:
    fieldnames = ['repo_name']
    writer = csv.DictWriter(wfile, fieldnames=fieldnames)
    #writer = csv.writer(wfile)
    #writer.writerows(lencommits)
    writer.writeheader()
    for i in repolist:
        writer.writerow({'repo_name':i})

length = len(repolist)

# ?page=1&?access_token=6eb9643ba09cea0ca71abcfd88b81aea3f5a65d1
collaborators =[]
contributions =[]
repos =[]
for i in range(0,length):
    url = "https://api.github.com/repos/mozilla/{}/contributors?page=1&per_page=1000".format(repolist[i])
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
#print(collaborators)

with open('repousersdetails.csv','w',newline='',encoding="utf-8") as wfile:
    fieldnames = ['repo_name', 'username','no_of_contributions']
    writer = csv.DictWriter(wfile, fieldnames=fieldnames)
    #writer = csv.writer(wfile)
    #writer.writerows(lencommits)
    writer.writeheader()
    for i,j,k in zip(repos, collaborators, contributions) :
        writer.writerow({'repo_name':i, 'username':j , 'no_of_contributions': k})
print("completed")
