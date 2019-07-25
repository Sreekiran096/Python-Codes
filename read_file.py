# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 13:48:21 2019

@author: vadaga
"""

import pandas as pd
import feather

def read_file(path):
    if '.csv' in path:
        data = pd.read_csv(path)
    elif '.xlsx' in path:
        data = pd.read_excel(path)
    elif '.feather' in path:
        data = feather.read_dataframe(path)
    else:
        print("No file with the mentioned path {}".format(path))
    return data

path = input('Path for the file to read: ')
print("path is given {}".format(path))
data = read_file(path)