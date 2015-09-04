from __future__ import print_function
from numpy import *
from pylab import *
from decimal import *

import os
import random
import sys
import numpy
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
	
f1= readfile('/home/icub/Desktop/1hzsinglesinusoidal.txt',0)
size = len(f1)
timestamp = zeros(size,int)

for i in range(0,size): #doing for loop until the size of the data
    data2 = f1[i].rsplit("\n") #splitting the data
    data_split = data2[0].split()#removing the spaces
    timestamp[i] = hex2dec(data_split[1])

print('datasplit \n',timestamp)


x = np.arange(size)
y = np.sin(2 * np.pi * timestamp*x )
plt.plot(x,y)
plt.show()