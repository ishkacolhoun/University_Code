#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:12:28 2021

@author: ishka
"""

#list stack
#make a stack empty
# list_1 = [1,2,3,4]
# list_1.clear()
# print(list_1)

# #add an element to the top of the stack
# list_1 = [3,2,1,4]
# list_1.append(5)
# print(list_1)

# #remove (pop) top element in the stack
# list_1 = [1,2,3,4]
# list_1.pop()
# print(list_1)

# # push an element to the top of the stack
# list_1 = [1,2,3,4,5]
# list_1.append(list_1[2])
# list_1.pop(2)
# print(list_1)

#list queue
# #adding to the queue
# queue = [1,2,3,4]
# queue.insert(0,5)
# print(queue)

# #removing from the queue
# queue = [0,1,2,3,4]
# queue.pop()
# print(queue)

# from collections import deque
# using deque for stacks and queue's

# deque_1 = deque([1,2,3,4,5])
# print(deque_1)


# problems:
#iterative linear search
# def itlinsearch(x,list):
#     i = 0
#     while list[i] != x:
#         i = i + 1
#     return i
# list_1 = []
# print(itlinsearch(5,list_1))

#recursive linear search
# def reclinsearch(x,list,i):
#     if i < 0:
#         return -1
#     elif x == list[i]:
#         return i
#     else:
#         return reclinsearch(x, list,i-1)
       
      
# list_1 = (2,1,4,5)
# print(reclinsearch(1,list_1,3))

#iterative binary search (list must be sorted)

# def itbinsearch(list,x):
#     temp = list
#     n = len(list)//2
#     while n >= 0:
#         if temp[n] == x:
#             return n
#         elif temp[n] > x:
#             temp = temp[:len(temp)//2]
#         else:
#             temp = temp[len(temp)//2:]
#         n = len(temp)//2

# list_1 = [1,2,3,4,5,8]
# print(itbinsearch(list_1, 5))

# list1 = [1,2,3,4,5,6,7,8,9]
# search = 1
# temp = list1
# n = len(list1)//2
# while n != 0:
#     if temp[n] == search:
#         print('result at index',n)
#         n = 0
#     elif temp[n] > search:  # if search to the left
#         temp = temp[:len(temp)//2]
#         print('a',n,temp)
#         n = len(temp)//2
        
#     else:                  # if search to the right
#         temp = temp[len(temp)//2:]
#         print('c')
#         print('c',n,temp)
#         n = len(temp)//2


# #recursive binary search
# list1 = [1,2,3,4,5]
# def recbinsearch(listn,search):
#     temp = listn
#     n = len(temp)//2
#     if temp[n] == search:
#         return n
#     elif temp[n] > search:  #its left
#         temp = temp[:len(temp)//2]
#         return recbinsearch(temp, search)
#     else:                   # its right
#         temp = temp[len(temp)//2:]
#         return recbinsearch(temp, search)
        
    
# print(recbinsearch(list1,4))

test1 = [-2, 0, 3, 7, 8, 10]
target = 10
#finds middle of list
def binsearch(test,low,high,target):
    if high >= low:
        mid = (high+low)//2
        if target == test[mid]:
            return mid
        elif target > test[mid]: # if on right
            return binsearch(test,mid + 1,high,target)
        else:
            return binsearch(test,low,mid-1,target)
    else:
        return -1
print(binsearch(test1, 0, 3, target))



#merges usorted list

# list1 = [1,3,5]
# list2 = [5,6,0,3]
# list3 = list1 + list2
# print(sorted(list3))

# # checks 2 lists for equality(recursively)
# def equal(list1,list2,i):
#     x = 1
#     while len(list1) < i or len(list2) < i:
#         if list1[i] == list2[i]:
#             return equal(list1,list2,i-1)
#             x = x * 1
#         else:
#             x = x * 0 
#         return x

# a = [1,2,3,4]
# b = [1,2,3,4]
# print(equal(a,b,3))


# selection sort

# list1 = [-1,4,2,1,1,9,0]
# for j in range(len(list1)):
#     for i in range(len(list1)):
#         if list1[j] < list1[i]:
#             list1[j], list1[i] = list1[i], list1[j]
# print (list1)

# #swaps elements in a list
# list1 = ['abc','def','ghi',4]
# for i in range(len(list1)//2):
#     list1[i], list1[len(list1)-i-1] = list1[len(list1)-i-1],list1[i]
# print(list1)


# merge sort








