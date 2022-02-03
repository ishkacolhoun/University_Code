#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:13:26 2021

@author: ishka
"""

''' THIS FUNCTION DEFINES WHAT LANGUAGE THE INPUTTED TEXT IS IN '''

def function2(probability_german,probability_english):

    print('\nEnter some text\n')
    text = input()
    j=0
    k= 0

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    count =[0]*28
    probability = [0]*28
    list1 = [0]*28
    list2 = [0]*28

    for i in text:
        if i != ' ':
            k = k+1
    print('\nYou have entered', k ,'characteres' )

    for i in text:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                count[j] = count[j]+1
            
    for i in range(len(alphabet)):
                probability[i] = count[i]/k
        
        
    for i in range(26):
        if probability[i] > probability_english[i]:
            list1[i] = probability[i] - probability_english[i]
        elif probability[i] < probability_english[i]:
            list1[i] = probability_english[i] - probability[i]
            
            
    for i in range(26):
        if probability[i] > probability_german[i]:
            list2[i] = probability[i] - probability_german[i]
        elif probability[i] < probability_german[i]:
            list2[i] = probability_german[i] - probability[i]
            

    if sum(list1)< sum(list2):
        print('Your text is in english')
    else:
        print ('Your text is in german')


''' THIS FUNCTION DEFINES THE PROBABILITY OF EACH LETTER COMING UP IN A 
GERMAN AND ENGLISH TEXT '''


def function1 (text_german, text_english):
    charactere_german = 0
    charactere_german = len(text_german)
    
    charactere_english = 0
    charactere_english = len(text_english)
    
    count_english =[0]*28
    count_german =[0]*28
    probability_english = [0]*28
    probability_german = [0]*28
    
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    
    print("A total of",charactere_german, "german characteres are available in the file(s)")
    print("A total of",charactere_english, "english characteres are available in the file(s)")
    
    for i in text_german:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                count_german[j] = count_german[j]+1
            
    for i in range(len(alphabet)):
        probability_german[i] = count_german[i]/charactere_german
    
    
    for i in text_english:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                count_english[j] = count_english[j]+1
            
    for i in range(len(alphabet)):
        probability_english[i] = count_english[i]/charactere_english
        
    function2(probability_german,probability_english)

    
'''THIS PART OF THE CODE OPENS AND READ THE MAIN FILE'''
    
slash = '\\'
entire_text_english = ''
entire_text_german = ''
print ('what is your file location')
location= input()

print ('what is your file name')
name = input()

variable1 = open(location+slash+name, "r")
count = len(open(location+slash+name).readlines())


''' THIS PART OF THE CODE DETECT WHAT LANGUAGE EACH INDIVIDUAL FILE IS IN'''

for i in variable1:
    variable2 = location+slash+i
    variable2 = variable2[:-1]
    
    if i[0] == 'g':
        text = open(variable2, "r")
        for x in text:     
            entire_text_german = entire_text_german + x
        
        
        
    elif i[0] == 'e':
        text = open(variable2, "r")
        for x in text:     
            entire_text_english = entire_text_english + x
               
               
               
function1(entire_text_german,entire_text_english)