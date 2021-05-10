import requests
import json
import csv
import pprint
#import sys
import pandas as pd

users_data = pd.read_csv('sorted_repousers.csv')
print(users_data.describe())

repo_commits = pd.read_csv('total_commits.csv')
#print(data.describe())

uname = "Bharathbrothers"
token = "6eb9643ba09cea0ca71abcfd88b81aea3f5a65d1"

#username = users_data['username']
reponame = repo_commits['repo_name']
contricount = repo_commits['no_of_contributions'] # no of commits
size = len(contricount)

#get total number of commits by counting all contributions of all users to a particular repo which is true in 99%
#cases unless when a person leaves an organization

#count_commits = []
total_df = pd.DataFrame()

df_list =[]
pullsid =[]
pullsbody =[]
for i in range(61,size):
    commitid = []
    commitmsg =[]
    commitauthor =[]
    commitauthordate =[]
    comauthorlogin =[]
    shaauthorlogin =[]
    stats_total = []
    stats_addns =[]
    stats_delns = []

    num = int((contricount[i] / 100)+1)
    for j in range(1,num+1): # check this to num+1 ?
        url = "https://api.github.com/repos/mozilla/{}/commits?page={}&per_page=100".format(reponame[i],j)
        get_data = requests.get(url,auth = (uname,token)).json()
        #get_data = json.loads(getting_data)
        j0=0
        j1=0
        j2=0
        #pprint(get_data)
        #print(username[i])
        #print(reponame[i])
        #print(len(get_data))
        for each in get_data:
            commitid.append(each['sha'])
            commitmsg.append(each['commit']['message'])
            commitauthor.append(each['commit']['author']['name'])
            commitauthordate.append(each['commit']['author']['date'])
            try:
                comauthorlogin.append(each['author']['login'])
            except:
                comauthorlogin.append(each['commit']['author']['name'])
            sha = each['sha']
            print(each['sha'])
            #print(each['commit']['message'])
            #print(each['commit']['author'])
            sha_url = "https://api.github.com/repos/mozilla/{}/commits/{}".format(reponame[i],sha)
            print(sha_url)
            sha_data = requests.get(sha_url,auth = (uname,token)).json()
            #sha_data = json.loads(shade_data)
            #for item in :
                #try:
            try:
                shaauthorlogin.append(sha_data['author']['login'])
            except:
                shaauthorlogin.append(sha_data['commit']['author']['name'])
            stats_total.append(sha_data['stats']['total'])
            stats_addns.append(sha_data['stats']['additions'])
            stats_delns.append(sha_data['stats']['deletions'])
            print(sha_data['stats']['total'])
                #except:
                  #  pass
    list_data = list(zip(commitid, commitmsg,commitauthor,commitauthordate,comauthorlogin,shaauthorlogin,stats_total,stats_addns,stats_delns)) #  removed
    df_r = pd.DataFrame(list_data, columns = ['commitid', 'commitmsg','commitauthor','commitauthordate','comauthorlogin','shaauthorlogin','stats_total','stats_addns','stats_delns'])  
    df_r.to_csv('commits_'+reponame[i]+'_details.csv',sep=',', encoding='utf-8')
    df_list.append(df_r)
    print(i,': completed')
            #j0=j0+1
            #cc=cc+1
'''
        url = "https://api.github.com/repos/mozilla/{}/pulls?page={}&per_page=1000".format(reponame[i],j)
        get_data = requests.get(url,auth = (uname,token)).json()
        #pprint(get_data)
        #print(len(get_data))
        for k in get_data:
            pullsid.append(k['url'])
            pullsbody.append(k['body'])
            print(k['url'])
            print(k['body'])
            #j2=j2+1
            #cp=cp+1

    for c in range(0,j0):
        finaluserc.append(username[i])
        finalrepoc.append(reponame[i])
    for c in range(0,j1):
        finaluseri.append(username[i])
        finalrepoi.append(reponame[i])
    for c in range(0,j2):
        finaluserp.append(username[i])
        finalrepop.append(reponame[i])
'''

total_df = pd.concat(df_list,ignore_index=True)        
total_df.to_csv('final_commits_details.csv',sep=',', encoding='utf-8')

#write data    

