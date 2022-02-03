#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:49:45 2021

@author: ishka
"""

import math as math # imports the math libraries
import numpy as np  #imports the numpy libraries
import cmath as cm  #imports the cmath libraries
import scipy as sp  #imports the scipy libraries
from scipy import optimize  #imports optimise from the scipy libraries
import matplotlib.pyplot as plt  #imports the matplotlib.pylot libraries

'''-----------------------------------------------------------------------'''

filename = input('Data file name (including extension): ') # takes input and assigns it to the variable filename
  
my_file = open(filename) # opens the file with the data

temp_data=[] # creates an empty list called temp_data

for line in my_file:  #runs a for loop iterating through every line in the data file(my_file)
    x, y = line.split(',') #splits each line into two different values x and y
    temp_data += [float(x), float(y)]  # converts the data points to floats.
    # the above converts the csv file into the list temp_data
my_file.close() # closes the file my_file

data_set = np.array(temp_data) # turns the list temp_data into a np.array called data_set
# the below creates two new arrays called x_data and y_data
x_data = data_set[0::2] # assigns every second data point from the array data_set starting from index 0 to the array x_data
y_data = data_set[1::2] # assigns every second data point from the array data_set starting from index 1 to the array y_data
N=len(x_data) # assinging N the value of however many data points there are in the x_data array
'''-----------------------------------------------------------------------'''

'''-----------------------------------------------------------------------'''
inpA0 = input('Initial guess for A: ') #inputs your guess for A
inpB0 = input('Initial guess for B: ') # inputs your guess for B
inpC0 = input('Initial guess for C ') # inputs your guess for C
A0=float(inpA0) #converts your guesses to floats
B0=float(inpB0) #converts your guesses to floats
C0=float(inpC0) #converts your guesses to floats

init_guess = np.array([A0,B0,C0]) # making an array called init_guess made up of your initial guesses

def non_lin_fit(par): #defining a function called non_lin_fit
    A=par[0] #giving A the first value in the list par
    B=par[1] #giving B the second value in the list par
    C=par[2] #giving C the third value in the list par
    squared_diff = (((A+B*(math.e**(-x_data/C)))-y_data)**2) # we changed this to the formula we were 
                                                             #given for our function instead of the linear function
    sum_squares = np.sum(squared_diff) #summing the square of the errors on y up
    return sum_squares #the function returns the sum_squares value

best_fit = sp.optimize.fmin(non_lin_fit, init_guess) #finding the minumum values for non_lin_fit using the scipy function optimize
print("Best fit value of A = ",best_fit[0]) # prints the value of A,B and C 
print("Best fit value of B = ",best_fit[1],'Best fit value of C= ',best_fit[2])                                                                                      
'''-----------------------------------------------------------------------'''
s