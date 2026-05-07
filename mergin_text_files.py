#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:16:06 2026

@author: aslanboncuk
"""


#%%

#Following python code will merge individual .txt files into one single .txt file.

''' For spike protein sequences '''
'''
import glob
filenames_Spike = glob.glob("*.txt")    #this code retrieves the name of each .txt file in the directory.


#Merging individual files into one single text file.

with open('/Users/aslanboncuk/Desktop/Bioinformatics_project/all_spike_merged.txt', 'w') as output:
    for filename in filenames_Spike:
        with open(filename) as input_file:
            output.write(input_file.read())
'''
        
#%%



''' For spike protein sequences '''

import glob


filenames_Nucleocapsid = glob.glob("*.txt")    #this code retrieves the name of each .txt file in the directory.


#Merging individual files into one single text file.

with open('/Users/aslanboncuk/Desktop/Bioinformatics_project/all_nucleocapsid_merged.txt', 'w') as output:
    for filename in filenames_Nucleocapsid:
        with open(filename) as input_file:
            output.write(input_file.read())
        








