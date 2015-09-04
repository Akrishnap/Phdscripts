# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
from numpy import *
from pylab import *
from decimal import *

import os
import random
import sys
import numpy as np
import getopt
import string
import matplotlib.pyplot as plt
import array
import pylab
import matplotlib
import time
import binascii

def readfile(filename,buffer):
	'''Print a file to the standard output.'''
	arr = []
	f = file(filename)
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		arr.append(line)
		buffer = buffer + 1
		#print line,buffer     # notice comma
	f.close()
	return arr
	
def dec2hex(n):
	#
	"""return the hexadecimal string representation of integer n"""
	#
	return "%X" % n
	

#
def hex2dec(s):
	#
	"""return the integer value of a hexadecimal string s"""
	#
	
        return int(s, 16)

def int2bin(n, count=24):
	#
	"""returns the binary of integer n, using count number of digits"""
	#
	return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])
		
f = readfile('/home/icub/Desktop/1hzsinglesinusoidal.txt',0)
size = len(f)
timestamp = zeros(size,int)
address1 = zeros(size,int)

for i in range(0,size):
    data2 = f[i].rsplit("\n")
    #print('data 2 \n',data2)
    data_split = data2[0].split()
    address = data_split[0]
    timestamp[i] = hex2dec(data_split[1])


    #data_split = data2[0].split(' ') #removing the spaces

    #print("adr: '"+address+"'")
    address1[i] = hex2dec(address)
    #print('address \n',address1)
    #print('time \n',timestamp)

#timestamp = (timestamp - timestamp[0])/1000000
print('timestamp \n',timestamp[1])
t = arange(0,5,0.01)
#sig = 3.3 * sin(2*np.pi*1*timestamp)
sig = 3.3*sin(2*np.pi*1*t)
plt.subplot(2,1,1)
plt.plot(t,sig)
plt.subplot(2,1,2)
plt.plot(timestamp/1000000000,address1,'ro')
#plt.xlim(0,100)
#plt.xlabel('time')
plt.show()