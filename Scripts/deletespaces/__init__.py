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
	
f = readfile('/home/icub/Desktop/1hzsinusoidal.txt',0)
f1 = readfile('/home/icub/Desktop/1hzsquarewave.txt',0)
#f2 = readfile('/home/icub/Desktop/sine3.3/100hz.txt',0)
#f3 = readfile('/home/icub/Desktop/sinewaveamp5/add2/1khz.txt',0)
#f4 = readfile('/home/icub/Desktop/sinewaveamp3.3/add2/10khz.txt',0)
writer = open('/home/icub/Desktop/1hzsinusoidalmod.txt','w+')
writer1 = open('/home/icub/Desktop/1hzsquarewave.txt','w+')
#writer2 = open('/home/icub/Desktop/sine3.3/100.txt','w+')
#writer3 = open('/home/icub/Desktop/sine3.3/add2/1k.txt','w+')
#writer4 = open('/home/icub/Desktop/sine3.3/add2/10k.txt','w+')
size = len(f)
size1 = len(f1)
#size2 = len(f2)
#size3 = len(f3)
#size4 = len(f4)
for i in range(0,size):
    data2 = f[i].rsplit("\n")

    data_split = data2[0].split()

    writer.write(data_split[0]+ " " +data_split[1] +"\n")
for i in range(0,size1):
    data2 = f1[i].rsplit("\n")

    data_split = data2[0].split()

    writer1.write(data_split[0]+" "+data_split[1] +"\n")
#for i in range(0,size2):
#    data2 = f2[i].rsplit("\n")

 #   data_split = data2[0].split()

 #   writer2.write(data_split[0]+" "+data_split[1] +"\n")
'''
for i in range(0,size3):
    data2 = f3[i].rsplit("\n")

    data_split = data2[0].split()

    writer3.write(data_split[0]+" "+data_split[1] +"\n")
for i in range(0,size4):
    data2 = f4[i].rsplit("\n")

    data_split = data2[0].split()

    writer4.write(data_split[0]+" "+data_split[1] +"\n")
'''


