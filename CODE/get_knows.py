import requests
import json
import csv
import pprint
import os
#import sys
import pandas as pd


first_sorted_dataset = pd.read_csv('first_sorted_incomplete_less_row_dataset.csv')

print(first_sorted_dataset.describe())
print(first_sorted_dataset.shape)
print(first_sorted_dataset.nunique())
print(first_sorted_dataset['ft_uname'].unique())
print(pd.unique(first_sorted_dataset['ft_uname']))

print(first_sorted_dataset['ft_rname'].unique())
print(pd.unique(first_sorted_dataset['ft_uname']))
print(first_sorted_dataset.count())
'''
print('pullauthor date: ', pd.unique(first_sorted_dataset['pullauthordate']))
print('ft commit author date: ',pd.unique(first_sorted_dataset['ft_commit_date']))
print('commit author date: ',pd.unique(first_sorted_dataset['commitauthordate'])) 
print('commit id:  ',pd.unique(first_sorted_dataset['commitid']))
'''
#first_sorted_group_username =
count_df = pd.DataFrame()
print(first_sorted_dataset['ft_uname'].value_counts(ascending=True))
print(first_sorted_dataset['ft_rname'].value_counts(ascending=True))

'''uname = first_sorted_dataset['ft_uname'].unique()

c =0
for i  in uname:
    if i == first_sorted_dataset['ft_uname']
'''
#groupby('ft_uname')
first_sorted_dataset = first_sorted_dataset.drop_duplicates(subset='ft_commit_date', keep="first")
#first_sorted = first_sorted.drop(first_sorted.index['',''])
final_ten_incomplete = first_sorted_dataset.groupby('ft_uname').head(10)
#df = df.set_index(['mainid','pidy']).groupby('pidx')['score'].nlargest(2).reset_index() 
final_ten_incomplete.to_csv('final_ten_incomplete_final_150.csv',sep=',', encoding='utf-8')
print(final_ten_incomplete.nunique())

