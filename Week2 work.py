#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:20:37 2021

@author: ishka
"""

# list_1 = []
# if len(list_1) == 0:
#     print('empty')
# else:
#     print('not empty')

# list_2 = [1,4,3,1]
# list_1 = [3,3,3,0]
# list_2.insert()
# print(list_2)

# list_3 = [1,2,3,4]
# list_3.remove(list_3[-2])
# print(list_3)

# m = [1,2,4]
# list_5 = [2,4,5,1]
# list_5 = list_5 + m
# print(list_5)

# recursive factorial function

# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*fac(n-1)

# simple iterative power algorithm

# b = int(input('base: '))
# n = int(input('power: '))
# p = 1
# for i in range(0,n):
#     p = p * b
# print(p)

# simple recursive power algorithm


# def power(b,n):
#     if n == 0:
#         return 1
#     else:
#         return b*power(b,n-1)

# smart iterative power algorithm

# b = 3
# n = 3
# p = b
# m = n
# while n > 0:
#     if n % 2 != 0:
#         p = p * b
#         print('odd')
#         print(p)
#     else:
#         p = p
#         n = int(n / 2)
#         p = p * p
#         print('even')
#         print(p)
#     n = n - 1
# print(p)
    
    
            
# b = 3
# n = 5
# p = b
# n = n - 1
# while n > 0: # runs until n is = 0 or smaller
#     if n % 2 != 0: # checks if odd
#         print('odd initial n =',n,'p =',p)
#         p = p * b  # multiplies bass by p
#         n = n - 1 #reduces n by one
#         print('odd final n =',n,'p =',p)
#     else:
#         print('even n =',n,'p =',p)
#         p = p * p #squares p if n even
#         n = n / 2 # divides n by 2
#         n = int(n)
#         print('even final n =',n,'p =',p)
# print(p)
            

# p = 1
# b = 3
# q = 3
# n = 6
# m = n
# while m > 0:
#     if m % 2 != 0:
#         p = q * p
#         m = m - 1
#     else:
#         p = p * p
#         m = int(m/2)
# print(p)

    
# p = 1
# b = 3
# q = 3
# n = 6
# m = n
# while m > 0:
#     if m % 2 != 0:
#         p = q * p
#     else:
#         p = p
#     p = p * p
#     m = int(m/2)
# print(p)

 # prints sum of first n odd numbers (iterative)
x = 0
n = 500
for i in range(1,2*n,2):
    x = i + x
print(x)


# prints sum of first n odd numbers (recursive)
# def sum_odd(n):
#     if n == 1:
#         return 1
#     else:
#         m = 2*n - 1
#         return m + sum_odd(n - 1)

# print(sum_odd(6))
    


 # a function that returns the sum of all even numbers between m and n (including m and n) where m and n are positive integers and m ≤ n     

# x = 0
# n = 8
# m = 3
# if m % 2 != 0:
#     m = m + 1
# else:
#         m = m
# for i in range(m,n+1,2):
#     x = i + x
# print(x)

# checks if a string is a pallindrome

# word = 'dod'
# b = bool(True)
# if len(word) % 2 == 0:
#     for i in range(0,int(len(word)/2) - 1):
#         x = bool(word[i]  == word[len(word)-i - 1])
# else:
#     n = int(len(word)/2)
#     for i in range(0,n):
#        x = bool(word[n + i] == word[n - i])
#        b = x * b
# print(bool(b))
        




