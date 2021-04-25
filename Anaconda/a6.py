# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:23:11 2020

@author: ASUS
"""

import numpy as np

population_std = np.random.randn(30)
print("The 30 random population is = ",population_std)

sample_std = np.random.choice(population_st,10)
print("The randomly choice of 10 population is = ",sample_std)

result_std = np.std(population_std)
result_std_sapmple = np.std(result_std)

print("Standard Deviatiion for population is = ",result_std)
print("Standard Deviation for sample population is = ",result_std_sapmple)
