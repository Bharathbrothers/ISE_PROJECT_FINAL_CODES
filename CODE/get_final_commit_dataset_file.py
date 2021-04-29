import requests
import json
import csv
import pprint
import os
#import sys
import pandas as pd
import glob

commits_path = r'C:\Users\stark\ise_project_code\finaltemp\commits'
#pulls_path = r'C:\Users\stark\ise_project_code\temp\pulls_data'

commits_files = glob.glob(commits_path + "/*.csv")
#pulls_files = glob.glob(pulls_path + "/*.csv")

com_list = []
#pull_list = []

for file_name in commits_files:
    df = pd.read_csv(file_name, header =0)
    com_list.append(df)
'''
for file_name in pulls_files:
    df = pd.read_csv(file_name, index_col = None, header =0)
    df['filename'] = (os.path.basename(file_name)).split('_')[1].split('_')[0]
    pull_list.append(df)
'''
commits_dataset = pd.concat(com_list, ignore_index = True)
commits_dataset.to_csv('commits_dataset_of_1064.csv',sep=',', encoding='utf-8')
'''
pulls_dataset = pd.concat(pull_list, ignore_index = True)
pulls_dataset.to_csv('pulls_dataset.csv',sep=',', encoding='utf-8')
'''
