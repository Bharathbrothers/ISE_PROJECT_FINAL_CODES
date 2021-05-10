import requests
import json
import csv
#import pprint
#import sys
import pandas as pd

users_data = pd.read_csv('sorted_repousers.csv')
#print(users_data.describe())

repo_pulls = pd.read_csv('total_pulls.csv')
#print(data.describe())

uname = "Bharathbrothers"
token = "6eb9643ba09cea0ca71abcfd88b81aea3f5a65d1"

#username = users_data['username']
reponame = repo_pulls['repo_name']
contricount = repo_pulls['no_of_contributions'] # no of pulls
size = len(contricount)

#get total number of pulls by counting all contributions of all users to a particular repo which is true in 99%
#cases unless when a person leaves an organization

#count_pulls = []
total_df = pd.DataFrame()

df_list =[]
#pullsid =[]
for i in range(950,1001):
    pullid = []
    pullsbody =[]
    pulltitle =[]
    pulls_number =[]
    pullauthor =[]
    
    pullauthordate =[]
    pullsuserlogin =[]
    pullsuserid =[]
    
    shaauthorlogin =[]
    author_association =[]
    merged_status =[]
    stats_changed_files = []
    stats_addns =[]
    stats_delns = []

    pull_repo_desc =[]
    pull_repo_lang =[]
    
    pull_commit_sha = []
    pull_commit_message =[]
    

    num = int((2000 / 100)+1)
    for j in range(1,num+1): # check this to num+1 ?
        url = "https://api.github.com/repos/mozilla/{}/pulls?state=all&page={}&per_page=100".format(reponame[i],j)
        get_data = requests.get(url,auth = (uname,token)).json()
        if(len(get_data)<100):
            num = 1
            
        #get_data = json.loads(getting_data)
        j0=0
        j1=0
        j2=0
        #pprint(get_data)
        #print(username[i])
        #print(reponame[i])
        #print(len(get_data))
        for each in get_data:
            
            
            pullnum = each['number']
            #print(each['number'])
            #print(each['pull']['message'])
            #print(each['pull']['author'])
            num_url = "https://api.github.com/repos/mozilla/{}/pulls/{}".format(reponame[i],pullnum)
            #print(num_url)
            num_data = requests.get(num_url,auth = (uname,token)).json()
            
            repo_url = "https://api.github.com/repos/mozilla/{}".format(reponame[i])
            repo_data = requests.get(repo_url, auth = (uname,token)).json()

           

            pull_commit_url = "https://api.github.com/repos/mozilla/{}/pulls/{}/commits".format(reponame[i],pullnum)

            pull_commit_sha_data = requests.get(pull_commit_url,auth = (uname,token)).json()  
            for every in pull_commit_sha_data:

                pullid.append(each['url'])
                pulls_number.append(each['number'])
                pullsbody.append(each['body'])
                pulltitle.append(each['title'])
                pullsuserlogin.append(each['user']['login'])
                pullsuserid.append(each['user']['id'])
                pullauthordate.append(each['created_at'])
            
                stats_changed_files.append(num_data['changed_files'])
                stats_addns.append(num_data['additions'])
                stats_delns.append(num_data['deletions'])
                author_association.append(num_data['author_association'])
                merged_status.append(num_data['merged'])
                try:
                    pull_repo_desc.append(repo_data['description'])
                    pull_repo_lang.append(repo_data['language'])
                except:
                    pull_repo_desc.append('EMPTY')
                    pull_repo_lang.append('EMPTY')
                 
                pull_commit_sha.append(every['sha'])
                pull_commit_message.append(every['commit']['message']) 
            #print(num_data['changed_files'])
                #except:
                  #  pass
    list_data = list(zip(pullid, pulls_number, pulltitle,pullsbody,pullsuserlogin,pullsuserid,pullauthordate,author_association,merged_status,stats_addns,stats_delns,stats_changed_files,pull_repo_desc,pull_repo_lang,pull_commit_sha, pull_commit_message)) #  removed
    df_r = pd.DataFrame(list_data, columns = ['pullid', 'pulls_number','pulltitle','pullsbody','pullsuserlogin','pullsuserid','pullauthordate','author_association','merged_status','stats_addns','stats_delns','stats_changed_files','pull_repo_desc','pull_repo_lang','pull_commit_sha','pull_commit_message'])  
    df_r.to_csv('pulls_'+reponame[i]+'_details.csv',sep=',', encoding='utf-8')
    df_list.append(df_r)
    #print(i,': completed')
            #j0=j0+1
            #cc=cc+1

total_df = pd.concat(df_list,ignore_index=True)        
total_df.to_csv('final_pulls_details_901-1001.csv',sep=',', encoding='utf-8')

#write data 

