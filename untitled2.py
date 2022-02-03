#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 16:38:48 2021

@author: ishka
"""


# list1 = ['name','file','age']
# list2 = ['bob','alice']
# list3 = [33,44]
# list4 = [10,11]
# print(list1,'\n',list2,'\n',list3,'\n',list4)
# x = np.array
# alp = []
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# for char in alphabet:
#     char = 'probability of ' + char +':'
#     alp.append(char)
# print(alp)
    
# list1 = [[1,2,5],[3,4,5]]
# list1[0].append('hi')
# print(list1)

# x = open(input(),'r')
# print(x.read())
# stop = ''
# language_training_files = []
# while True:
#     training_file = input()
#     if training_file == stop:
#         break
#     else:
#         language_training_files.append(training_file)
# print(language_training_files)
# list1 = []
# while True:
#     training_file = input()
#     if training_file == '':
#         break
#     else:
#         list1.append(training_file)
# print(list1)


# content = []
# while True:
#     line = input()
#     if line:
#         content.append(line)
#     else:
#         break

# import sys
# list1 = []
# for s in sys.stdin:
#     s = s.replace('\n', '')
#     list1.append(s)
# print(list1)
language_training_files = ['sasa_txt','esa_txt']
for line in language_training_files:
    line  = line.split('_')
    print(line)

print(language_training_files)

# temp = []
# for line in language_training_files:
#     temp.append(line.split('_'))
# languages_testing = {temp[i][0] for i in range(0,len(temp))}
# language_training_files_organised = temp






















