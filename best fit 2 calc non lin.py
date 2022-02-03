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
inpA0 = input('Initial guess for A: ') #inputs your guess for A
inpB0 = input('Initial guess for B: ') # inputs your guess for B
inpC0 = input('Initial guess for C ') # inputs your guess for C
A0=float(inpA0) #converts your guesses to floats
B0=float(inpB0) #converts your guesses to floats
C0=float(inpC0) #converts your guesses to floats

init_guess = np.array([A0,B0,C0]) # making an array called init_guess made up of your initial guesses

'''-----------------------------------------------------------------------'''
'''-----------------------------------------------------------------------'''
def line(xdata,A,B,C):
    return (A+B*(math.e**(-x_data/C)))

best_fit, cov = sp.optimize.curve_fit(line, x_data, y_data,[A0,B0,C0])
fit_err = np.sqrt(np.diag(cov))

print("Best fit value of A using curve_fit = ",best_fit[0], "±", fit_err[0])
print("Best fit value of B using curve_fit = ",best_fit[1], "±", fit_err[1])
print("Best fit value of C using curve_fit = ",best_fit[2], "±", fit_err[2])


'''-----------------------------------------------------------------------'''