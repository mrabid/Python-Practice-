# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:51:50 2020

@author: ASUS
"""

import statistics
import scipy.stats

dataset = [1,2,3,4,2,24,5,5,6,3,5,7,9,5,4,3,5,64,4,4,2,5,5]

mode1 = statistics.mode(dataset)
print("Mode using statistics = ",mode1)

mode2 = scipy.stats.mode(dataset)
print("Mode using scipy.stats = ",mode2)