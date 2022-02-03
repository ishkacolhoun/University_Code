#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:08:37 2021

@author: ishka
"""

import numpy as np  # imports the numpy library as np
import matplotlib.pyplot as plt # imports the pyplot function from the Matplotlib library
import math as math


filename = input('Data file name (including extension): ') # takes input and assigns it to the variable filename
  
my_file = open(filename) # opens the file located at the directory filename

temp_data=[] # creates an empty list called temp_data

for line in my_file: #runs a for loop iteratingthrough every line in the data file(my_file)
    x, y = line.split(',') #splits each line into two different values x and y
    temp_data += [float(x), float(y)] # converts the data points to floats.
    # the above converts the csv file into the list temp_data
my_file.close() # closes the file my_file

data_set = np.array(temp_data) # turns the list temp_data into a np.array called data_set
# the below creates two new arrays called x_data and y_data
x_data = data_set[0::2] # assigns every second data point from the array data_set starting from index 0 to the array x_data
y_data = data_set[1::2] # assigns every second data point from the array data_set starting from index 1 to the array y_data
# x=np.linspace(-np.pi,np.pi,101)
# y1=np.sin(x)+np.sin(3*x)/3.0
# y2=np.sin(x)
A = 4.931841090609264
B = 5.538453217807508
C = 6.363625649708868
x  = np.linspace(0,55)
y1 = (A+B*(math.e**(-x_data/C)))


plt.scatter(x_data,y_data)
plt.plot(x, y1)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Line of Best Fit Plot')