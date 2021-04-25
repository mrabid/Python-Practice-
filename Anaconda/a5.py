# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:49:58 2020

@author: ASUS
"""
#Variance

import numpy as np

population = np.random.randn(30)
print("The dandom population is = ",population)

sample = np.random.choice(population,20)
print("The 20 choice population out of random 30 is = ",sample)

result_population = np.var(population)
result_sample = np.var(sample)

print("Variance of population = ",result_population)
print("Variance of sample populatoin = ",result_sample)
