# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 23:53:47 2020

@author: ASUS
"""

import numpy as np

dataset = [9, 3, 2, 10, 30, 5, 13, 6, 4]

q1 = np.percentile(dataset, 25)
print("Q1 = ",q1)

q2 = np.percentile(dataset, 50)
print("Q2 = ",q2)

q3 = np.percentile(dataset, 75)
print("Q3 = ",q3)
