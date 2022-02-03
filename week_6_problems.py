#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:04:07 2021

@author: ishka
 """

# 1
# fileobject = open('/home/ishka/Desktop/Library/School/Physics/Year_2/Advanced_Programming/Program scripts/Test_Data.txt')
# text = fileobject.read()
# text = text.split('\n')
# print(text)

# letters_total = ''
# for letter in text:
#     letters_total = letters_total + letter

# set1 = {letter for letter in letters_total}
# for letter in set1:
#     print(letter, letters_total.count(letter))

#2 a

# Maths_Names =  set(open('/home/ishka/Desktop/Library/School/Physics/Year_2/Advanced_Programming/Program scripts/Maths_Names.txt').read().split())
# Physics_Names =  set(open('/home/ishka/Desktop/Library/School/Physics/Year_2/Advanced_Programming/Program scripts/Physics_Names.txt').read().split())
# print(Physics_Names)
# print(Maths_Names)
# All_Students = Maths_Names.union(Physics_Names)
# print(All_Students)

# 2 b + c 

# 3
# fileobject = open('/home/ishka/Desktop/Library/School/Physics/Year_2/Advanced_Programming/Program scripts/Grades.txt')
# list1 = fileobject.read()
# list1 = list1.split()
# student = []
# grade = []
# for i in range(0,len(list1),2):
#     student.append(list1[i])
#     grade.append(list1[i + 1])

# print(student)

# dict1 = dict()
# for i in range(0,len(student)):
#     dict1[student[i]] = {grade[i]}
    
# print(dict1[input()])


#4
# set1 = {1,4,6}
# list1 = [1,2,3,set1]
# print(list1)

#5
# deep copy
list1 = [1,2,3,4,0]
list2 = list1
list2[4] = 5
print('list1',list1,'\n','list2',list2)

# shallow copy
list1 = [1,2,3,4,0]
list2 = list1.copy()
list2[4] = 5
print('list1',list1,'\n','list2',list2)


