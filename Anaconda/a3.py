# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 22:28:37 2020

@author: ASUS
"""

import numpy

v = numpy.random.randint(5, 25, 15)
print("5 to 40 in 25 random value is = ",v)

r1 = numpy.max(v)
print("Max value is = ",r1)

r2 = numpy.min(v)
print("Min value is = ",r2)

r = r1 - r2
print("Result is = ",r)
