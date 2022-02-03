#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:04:39 2021

@author: ishka
"""


    # assigns training files names to lists
    
import sys
language_training_files = []
for file in sys.stdin:
    file = file.replace('\n', '')
    language_training_files.append(file)

    
    #splits language_training_files to view all languages being trained

temp = []
for line in language_training_files:
    temp.append(line.split('_'))
languages_testing = {temp[i][0] for i in range(0,len(temp))}
language_training_files_organised = temp


    # create a string for each line from language_training_files
text_list = ['' for i in range(0,len(languages_testing))]
x = 0
for language in languages_testing:
    i = 0
    for place in language_training_files_organised:
        if language == language_training_files_organised[i][0]:
            f = open(language_training_files[i],'r')
            text_list[x] = text_list[x] + f.read()
            text_list[x] = text_list[x].replace('\n','')
            f.close()
        i = i + 1
    x = x + 1
# print(character_list)
char_list = []
for text in text_list:
    text = [char for char in text]
    char_list.append(text)

# forms a list with sublists for each language containg the letter and its frequency
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
freq_list = []
for i in range(0,len(languages_testing)):
    freq_list.append([language_training_files_organised[i][0]])
    for letter in alphabet:
        freq_list[i].append(letter)
        freq = char_list[i].count(letter) / len(char_list[i])
        freq_list[i].append(freq)
# print(freq_list)

#prints output neatly
f = open('/home/ishka/Desktop/Library/School/Physics/Year_2/Advanced_Programming/Program scripts/Trained_Output.txt','w')
for j in range(len(languages_testing)):
    f.write(freq_list[j][0]+'\n')
    for i in range(1,len(freq_list[j]),2):
        f.write(str(freq_list[j][i+1])+'\n')
f.close()


# f = open('/home/ishka/Desktop/Library/School/Physics/Year_2/Advanced_Programming/Program scripts/Trained_Output.txt','w')
# for j in range(len(languages_testing)):
#     f.write(freq_list[j][0]+'\n')
#     for i in range(1,len(freq_list[j]),2):
#         f.write(str(freq_list[j][i+1])+'\n')
# f.close()
# prints output neatly
# for j in range(len(languages_testing)):
#      print('Probablities for: ',freq_list[j][0])
#      for i in range(1,len(freq_list[j]),2):
#         print(freq_list[0][i],'\t',freq_list[j][i+1])


    
    
    
    
    
    
    
    
    
    
    
    
    
# for language in languages_testing:
    
    
# for file in language_training_files:
#     f = open(file,'r')
#     english = english + f.read()
#     print(file)

# print(english)
# print(language_training_files)









