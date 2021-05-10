import requests
import json
import csv
import pprint
#import sys
import pandas as pd

reponame=[]
username =[]
noofcont= []

'''
with open('repousersdetails_UNIQUE.csv',newline='') as csvfile:
    reporead = csv.reader(csvfile,delimiter=',',quotechar='|')
    i=0
    for row in reporead:
        #print(','.join(row))
        reponame.append(row[0])
        username.append(row[1])
        noofcont.append(row[2])
        i=i+1
'''
data = pd.read_csv('repousersdetails_UNIQUE.csv')
print('no of unique contributors:', data['username'].nunique())
print('no of unique repositories:', data['repo_name'].nunique())
print('average no of contributions:', data['no_of_contributions'].mean())
print(data.describe())
unique_users = set(data['username'])
print(len(unique_users))
#print(unique_users)

#sort contributors and no of contributions
sort_data = data[['username','repo_name','no_of_contributions']]
print(sort_data.describe())
sort_data['no_of_contributions'] = sort_data['no_of_contributions'].astype(int) 
#sort_data.sort_values(by = 'no_of_contributions', ascending=False)
print(sort_data.describe())
print(len(sort_data['username']))
unique_sorted_data= sort_data.drop_duplicates('username')
print(len(unique_sorted_data['username']))
unique_sorted_data.sort_values(by='no_of_contributions', ascending=False, inplace=True)

unique_sorted_data.to_csv('unique_sorted_data_2.csv',sep=',', encoding='utf-8')
unique_top = unique_sorted_data[:1000]
unique_top.to_csv('unique_top1000_data_2.csv',sep=',', encoding='utf-8')
print(unique_top.head(10))
