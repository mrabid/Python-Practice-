# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 10:51:59 2020

@author: ASUS
"""

import numpy
import statistics

dataset = [1,2,3,4,5,7,9]
dataset1 = [1,2,3,4,6,7,8]

men = numpy.mean(dataset)
print("Mean using numpy = ",men)

men1 = statistics.mean(dataset)
print("Mean using statistics = ",men1)



medin = numpy.median(dataset1)
print("Median using numpy = ",medin)

medin1 = statistics.median(dataset1)
print("Median using numpy = ",medin1)

medin2 = statistics.median(dataset)
print("Median using numpy = ",medin2)
