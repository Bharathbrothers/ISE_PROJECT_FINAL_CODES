import requests
import json
import csv
import pprint
import pandas as pd

username = input('Enter your Organization name:')

repolist = []

uname = "Bharathbrothers"
token = "6eb9643ba09cea0ca71abcfd88b81aea3f5a65d1"

"""for k in get_data:
            fieldnames = list(k.keys())
            #fieldlist = list()
            writer = csv.DictWriter(wfile, fieldnames=fieldnames)
            #writer = csv.writer(wfile)
            #writer.writerows(lencommits)
            #print(fieldnames)
            writer.writeheader()
            z=0
            for i in k:
                s = fieldnames[z]
                d={}
                d[s]=k[i]
                #for key,val in d:
                writer.writerow({s:d[s]})
                #writerow({'repo_name':i})"""

for i in range(1,21):
    url = "https://api.github.com/orgs/"+username+"/repos?page={}&per_page=100".format(i)
    get_data = requests.get(url,auth = (uname,token)).json()
    print(len(get_data))
    for r in get_data:
        repolist.append(r["full_name"])
    with open('fullrepodetails.json', 'w',newline='',encoding="utf-8") as file:
        file.write(pprint.pformat(get_data))
    data = pd.json_normalize(get_data, max_level=1)
    print(data)
    if(i==1):
        totdata =[]
        totdata.append(data)
    else:
        totdata.append(data)
        #data.to_csv('fullrepodet.csv',sep='\t',encoding="utf-8")
    #with open('fullrepodet.csv','w',newline='',encoding="utf-8") as wfile:
    #    fieldnames = list(data.headers)
    #    writer = csv.DictWriter(wfile, fieldnames=fieldnames)
    #    writer.writeheader()
totdata = pd.concat(totdata,ignore_index=True)
totdata.to_csv('fullrepodet.csv',sep=',',encoding="utf-8")
    
print(len(repolist))
#print(repolist)

with open('repolist.csv','w',newline='',encoding="utf-8") as wfile:
    fieldnames = ['repo_name']
    writer = csv.DictWriter(wfile, fieldnames=fieldnames)
    #writer = csv.writer(wfile)
    #writer.writerows(lencommits)
    writer.writeheader()
    for i in repolist:
        writer.writerow({'repo_name':i})

