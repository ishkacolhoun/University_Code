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
inpm0 = input('Initial guess for slope, m0: ') #inputs your guess for slope
inpc0 = input('Initial guess for y-axis intercept, c0: ') # inputs your guess for y_intercept
m0=float(inpm0) #converts your guesses to floats
c0=float(inpc0) #converts your guesses to floats

init_guess = np.array([m0,c0]) # making an array called init_guess made up of your initial guesses

def lin_fit(par): #defining a function called lin_fit
    m=par[0] #giving m the first value in the list par
    c=par[1] #giving c the second value in the list par
    squared_diff = (((m*x_data)+c)-y_data)**2 # finds the square of the error on the y values
    sum_squares = np.sum(squared_diff) #summing the square of the errors on y up
    return sum_squares #the function returns the sum_squares value

best_fit = sp.optimize.fmin(lin_fit, init_guess) #finding the minumum values for lin_fit using the scipy function optimize
print("Best fit value of slope = ",best_fit[0], "Best fit value of intercept = ",best_fit[1]) # prints the value of best 
                                                                                              #fit for the slope and y-intercept
'''-----------------------------------------------------------------------'''
