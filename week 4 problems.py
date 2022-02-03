#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:18:08 2021

@author: ishka
"""
#Given a list of numbers, write a list comprehension that produces a copy of the list.
# list2 = [2,3,4,5]
# new = [i for i in list2]
# print(new)

#Given a list of numbers, write a list comprehension that produces a list of eeach numnber squared
# list2 = [2,3,4,5]
# new = [i**2 for i in list2]
# print(new) 


#Given a list of numbers, write a list comprehension that produces a list of the odd numbers in the list.

# list2 = [2,3,4,5,5,2,1]
# new = [i for i in list2 if i % 2 !=0]
# print(new)


#Given a list of numbers, write a list comprehension that produces a list of each odd number doubled.

# list2 = [2,3,4,5,5,2,1]
# new = [2*i for i in list2 if i % 2 !=0]
# print(new)

#opening files

    
fileobject = open('/home/ishka/Desktop/Library/School/Physics/Year_2/Advanced_Programming/Program scripts/Test_Data.txt')
temp = fileobject.read()
print(type(temp))
temp.split()
print(temp)
for i in range(len(temp)):
    xy = []
    xy = xy.append(int(temp[i]))
print(xy)


# prints the length of each word in a sentence
# fileobject = open('/home/ishka/Desktop/pydata.txt')

# list1 = fileobject.readline()
# list1 = list1.split()
# for i in range (len(list1)):
#     print(len(list1[i]))








