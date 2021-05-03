import requests
import json
import csv
import pprint
import os
#import sys
import pandas as pd


first_dataset = pd.read_csv('first_final_dataset_1000.csv')

first_sorted = first_dataset.sort_values(['ft_uname','ft_commit_date','ft_rname'],ascending =[True, True, True])

first_sorted = first_sorted.drop(first_sorted.index[[1,2]])
first_sorted.to_csv('first_final_sorted_1000.csv',sep=',', encoding='utf-8')
