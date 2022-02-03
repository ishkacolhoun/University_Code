#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 17:53:42 2021

@author: ishka
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 14:48:17 2021

@author: mathi
"""

# C:\Users\mathi\OneDrive\Desktop\Trained_Output.txt


def function2(probability_1a,probability_2a,languages):

    print('Enter some text\n')
    text = input()
    j=0
    k= 0

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    count =[0]*28
    probability = [0]*28
    list1 = [0]*28
    list2 = [0]*28
    
    
    probability_1 = [float(i) for i in probability_1a]
    probability_2 = [float(i) for i in probability_2a]
    
    for i in text:
            k = k+1
    
    
    for i in text:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                count[j] = count[j]+1
            
    for i in range(len(alphabet)):
                probability[i] = count[i]/k
        
        
    for i in range(len(alphabet)):
        if probability[i] > probability_2[i]:
            list1[i] = probability[i] - probability_2[i]
        elif probability[i] < probability_2[i]:
            list1[i] = probability_2[i] - probability[i]
            
            
    for i in range(len(alphabet)):
        if probability[i] > probability_1[i]:
            list2[i] = probability[i] - probability_1[i]
        elif probability[i] < probability_1[i]:
            list2[i] = probability_1[i] - probability[i]
    
    

    if sum(list1)< sum(list2):
        print('\nYour text is in' ,languages[0])
    else:
        print ('\nYour text is in', languages[28])
        
        
        
        
        
        
        

print ('what is your file location')
location= input()


variable1 = open(location, "r")
count = len(open(location).readlines())


''' THIS PART OF THE CODE DETECT WHAT LANGUAGE EACH INDIVIDUAL FILE IS IN'''

probability_language_1 = [0]*28
probability_language_2 = [0]*28

languages = variable1.readlines()

    
for i in range(1,28):
    probability_language_1[i] = languages[i]


for i in range(29,56):
    probability_language_2[(i-29)] = languages[i]

variable1.close()

function2(probability_language_1, probability_language_2, languages)