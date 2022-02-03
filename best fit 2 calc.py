#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:46:13 2021

@author: ishka
"""
import math as math
import numpy as np
import cmath as cm
import scipy as sp
from scipy import optimize
import matplotlib.pyplot as plt

'''-----------------------------------------------------------------------'''

filename = input('Data file name (including extension): ')
  
my_file = open(filename)

temp_data=[]

for line in my_file:
    x, y = line.split(',')
    temp_data += [float(x), float(y)]
    
my_file.close()

data_set = np.array(temp_data)

x_data = data_set[0::2]
y_data = data_set[1::2]
N=len(x_data)
    
'''-----------------------------------------------------------------------'''

'''-----------------------------------------------------------------------'''
inpm0 = input('Initial guess for slope, m0: ')
inpc0 = input('Initial guess for y-axis intercept, c0: ')
m0=float(inpm0)
c0=float(inpc0)

init_guess = np.array([m0,c0])

'''-----------------------------------------------------------------------'''

'''-----------------------------------------------------------------------'''

def line(xdata,m,c):
    return ((m*xdata)+c)

best_fit, cov = sp.optimize.curve_fit(line, x_data, y_data,[m0,c0])
fit_err = np.sqrt(np.diag(cov))

print("Best fit value of slope using curve_fit = ",best_fit[0], "±", fit_err[0])
print("Best fit value of intercept using curve_fit = ",best_fit[1], "±", fit_err[1])

'''-----------------------------------------------------------------------'''