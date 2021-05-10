import requests
import json
import csv
import pprint
import os
#import sys
import pandas as pd
import glob

first_path = pd.read_csv('first_final_dataset_1000.csv')

#first_files = glob.glob(first_path + "/*.csv")

#first_list =[]
'''
for file_name in first_files:
    df = pd.read_csv(file_name, header =0)
    first_list.append(df)

first_dataset = pd.concat(first_list, ignore_index = True)
'''
#print(first_dataset.nunique())
first_dataset = first_path.drop_duplicates(ignore_index =True)
first_dataset.to_csv('first_complete_dataset_1000.csv',sep=',', encoding='utf-8')


