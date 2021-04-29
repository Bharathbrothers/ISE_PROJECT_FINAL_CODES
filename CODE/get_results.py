import requests
import json
import csv
import pprint
# os
#import sys
import pandas as pd

commits_dataset = pd.read_csv('commits_dataset.csv')

pulls_dataset = pd.read_csv('pulls_dataset.csv')

#pulls_user_login = pulls_dataset['pullsuserlogin']

first_ten_df = pd.DataFrame()
df_list =[]

ft_uname =[]
ft_rname =[]
ft_commit_date =[]
author_association = []
merged_status = []
ft_total_changes = []
ft_addns =[]
ft_delns =[]
pull_title =[]
pull_msg =[]
pullauthordate =[]
pullid = []
commitauthordate =[]
commitid =[]
pullcommitsha =[]
pullcommitmsg =[]
repodesc =[]
repolang =[]

'''Name
Commit Message
Commit Date
Link to Commit
Files Changed
Total no of lines changed (added+deleted)
Lines added
Lines deleted
Link to pull request
Title for pull request
Pull request message
Author Association
Pull request created
Pull request closed
Description of repository
Main language of repo
License
'''

for i_index, i in pulls_dataset.iterrows():
    user_name = i['pullsuserlogin']
    reponame = i['filename']
    for j_index, j in commits_dataset.iterrows():
        if j['reponame']==reponame and j['comauthorlogin'] == user_name and i['merged_status']==True and i['pull_commit_sha']==j['commitid']:
            ft_uname.append(user_name)
            ft_rname.append(reponame)
            ft_commit_date.append(j['commitauthordate'])
            author_association.append(i['author_association'])
            merged_status.append(i['merged_status'])
            pull_title.append(i['pulltitle'])
            pull_msg.append(i['pullsbody'])
            pullauthordate.append(i['pullauthordate'])
            pullid.append(i['pullid'])
            ft_total_changes.append(j['stats_total'])
            ft_addns.append(j['stats_addns'])
            ft_delns.append(j['stats_delns'])
            commitauthordate.append(j['commitauthordate'])
            commitid.append(j['commitid'])
            pullcommitsha.append(i['pull_commit_sha'])
            pullcommitmsg.append(i['pull_commit_message'])
            repodesc.append(i['pull_repo_desc'])
            repolang.append(i['pull_repo_lang'])


    list_data = list(zip(ft_uname, ft_rname,ft_commit_date, author_association , merged_status, pull_title, pull_msg, pullauthordate,pullid, ft_total_changes, ft_addns, ft_delns, commitauthordate, commitid,pullcommitsha,pullcommitmsg,repodesc,repolang)) #  removed
    df_r = pd.DataFrame(list_data, columns = ['ft_uname', 'ft_rname','ft_commit_date','author_association' , 'merged_status', 'pull_title', 'pull_msg', 'pullauthordate','pullid', 'ft_total_changes', 'ft_addns', 'ft_delns', 'commitauthordate','commitid', 'pullcommitsha','pullcommitmsg','repodesc', 'repolang'])  
    df_r.to_csv('first_ten/first_ten_'+user_name+'_details.csv',sep=',', encoding='utf-8')
    df_list.append(df_r)
    #print(i,': completed')
            #j0=j0+1
            #cc=cc+1

total_df = pd.concat(df_list,ignore_index=True)        
total_df.to_csv('first_ten_final_total.csv',sep=',', encoding='utf-8')

