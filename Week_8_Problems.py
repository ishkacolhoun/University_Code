#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:18:51 2021

@author: ishka
"""

import numpy as np
import matplotlib.pyplot as plt
#1,2,3,4

# Amplitute = 0.5
# frequency = 2
# phase = np.pi
# omega = 2 * np.pi * frequency
# t = np.linspace(0,1,40000,dtype = 'float32')
# f = Amplitute * np.sin(omega * t + phase)
# g = Amplitute * np.sin(omega * t + phase)
# h = f + g
# plt.plot(t,h,color = 'green')
# plt.plot(t,f,color = 'blue')
#print(t.dtype)
 
#5

# from scipy.io.wavfile import write

# samplerate = 44000
# Amplitute = 3
# frequency = 500
# phase = np.pi
# omega = 2 * np.pi * frequency
# t = np.linspace(0,1,40000,dtype = 'float32')
# f = Amplitute * np.sin(omega * t + phase)
# plt.plot(t,f)
# write('testnoise.wav',40000,f)

#6

from scipy.io.wavfile import write

samplerate = 44000
Amplitute = 3
lamda = 3
frequency = 500
phase = np.pi
omega = 2 * np.pi * frequency
t = np.linspace(0,1,40000,dtype = 'float32')
f = Amplitute * np.exp(-lamda * t) * np.cos(omega * t)
plt.plot(t,f)
write('testnoise.wav',40000,f)