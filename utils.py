# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:39:46 2024

@author: 213
"""


import pandas as pd

def load_data():
    data = pd.read_csv('/BigData/data/LOCAL_PEOPLE_GU_UTF.csv')
    return data