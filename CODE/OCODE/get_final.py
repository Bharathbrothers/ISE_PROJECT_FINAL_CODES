import requests
import json
import csv
import pprint
#import sys
import pandas as pd

reponame=[]
username =[]
noofcont= []

data = pd.read_csv('repousersdetails.csv')
print(data.describe())

sort_data = data[['username','repo_name','no_of_contributions']]
d_sum = data[['repo_name','no_of_contributions']]
sum_data = d_sum.groupby(['repo_name']).agg({'no_of_contributions': 'sum'})
sort_data.sort_values(['username','repo_name'], ascending=[True,True], inplace=True)

sort_data.to_csv('sorted_repousers.csv',sep=',', encoding='utf-8')
sum_data.to_csv('total_commits.csv',sep=',', encoding='utf-8')
