#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:58:51 2021

@author: ishka
"""
import numpy as np
# #    Complex number
# r_a = float(input())
# theta_b = float(input())
# #if polar
# checker = np.sqrt()
# print(checker)


#truth table:
operator = input()
if operator == 'and':
    table = np.array([[0,0,1],[1,0,0],[0,1,0],[1,1,1]])
elif operator == 'or':
    table = np.array([[0,0,0],[1,0,1],[0,1,1],[1,1,1]])
elif operator == 'nand':
      table = np.array([[0,0,1],[1,0,1],[0,1,1],[1,1,0]])
print(table)
