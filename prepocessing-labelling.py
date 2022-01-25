# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 13:58:32 2021

@author: ARDI
"""

import os
import json
from shutil import copyfile

extracted_dir = 'C:/Users/ARDI/Documents/Tesis/Coswara-Data/Extracted_data'
list_date_dir = os.listdir(extracted_dir)
pos_dir = 'C:/Users/ARDI/Documents/Tesis/Coswara-Dat/Copy/pos'
neg_dir = 'C:/Users/ARDI/Documents/Tesis/Coswara-Dat/Copy/neg'
data_pakai = 'cough-shallow.wav'

def process_metadata(path):
    data = json.load(open(path))
    return data['covid_status']

def copy_data_batuk(path_batuk, path_metadata, person):
    if 'positive' in process_metadata(path_metadata):
        print('copy '+path_batuk+' to pos')
        copyfile(path_batuk, os.path.join(pos_dir, 'pos-'+person+'-'+data_pakai))
    elif 'healthy' in process_metadata(path_metadata):
        print('copy '+path_batuk+' to neg')
        copyfile(path_batuk, os.path.join(neg_dir, 'neg-'+person+'-'+data_pakai))
    
for date in list_date_dir:
    date_dir = os.path.join(extracted_dir, date)
    list_person_dir = os.listdir(date_dir)
    for person in list_person_dir:
        person_dir = os.path.join(date_dir, person)
        list_file = os.listdir(person_dir)
        if ('metadata.json' in list_file) and (data_pakai in list_file):
            batuk_file = os.path.join(person_dir, data_pakai)
            metadata_file = os.path.join(person_dir, 'metadata.json')
            copy_data_batuk(batuk_file, metadata_file, person)