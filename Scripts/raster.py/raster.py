from __future__ import print_function
from numpy import *
from pylab import *
from decimal import *

__author__ = 'icub'

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

# data = open('/home/icub/Documents/Phd/lab/Aishwarya/vnt/greenledwoutlight/onehz/dump.txt', "r+")
# rtext = data.read()
# print(rtext)
# print(len(rtext))

'''convert = rtext.encode("hex\n")
print(convert)
'''

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

#

def int2bin(n, count=24):
	#
	"""returns the binary of integer n, using count number of digits"""
	#
	return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

polMask = 1
xMask   = hex2dec("FE")
yMask   = hex2dec("7F00")
xShift  = 1
yShift  = 8

#rtext = readfile('/home/icub/Desktop/Ash/1hzdarkshuduse.txt', 0)
#rtext = readfile('/home/icub/Documents/Phd/research/lab/Aishwarya/vnt/greenledwoutlight/2hz/dump.txt', 0)
#rtext = readfile('/home/icub/Documents/Phd/lab/Aishwarya/vnt/greenledwoutlight/3hz/dump.txt', 0)
#rtext = readfile('/home/icub/Documents/Phd/lab/Aishwarya/vnt/greenledwoutlight/4hz/dump.txt', 0)
#rtext = readfile('/home/icub/Documents/Phd/lab/Aishwarya/vnt/greenledwoutlight/5hz/dump.txt', 0)
#rtext = readfile('/home/icub/Documents/Phd/lab/Aishwarya/vnt/greenledwoutlight/8.txt', 0)
#rtext = readfile('/home/icub/Documents/Phd/lab/Aishwarya/vnt/greenledwoutlight/10.txt', 0)
rtext = readfile('/home/icub/Documents/Phd/research/lab/Aishwarya/vnt/greenledwoutlight/20.txt', 0)
size = len(rtext)
print ("data length", size)

#Initialisation
# sizeYRaster = 144 * 72 * 12 * 2
# sizeXRaster = 144 * 72 * 12 * 2

timestamp = zeros(size,int)

#x = zeros(size,int)
#y = zeros(size,int)
xOn = zeros(size, int)
yOn = zeros(size, int)
xOff = zeros(size, int)
yOff = zeros(size, int)

polarity = zeros(size, int)

rasterAddr = zeros(size, int)

# xRaster = zeros(sizeXRaster, int)
# yRaster = zeros(sizeYRaster, int)

for i in range(0,size): #doing for loop until the size of the data
    data2 = rtext[i].rsplit("\n") #splitting the data
    #print("rtext \n",rtext[i])
    #print("data2 \n",data2)
    #data2 = rtext[i].split("\n")
    #print("data31 \n",data2)
    data_split = data2[0].split(' ') #removing the spaces

    address = data_split[0]
    #data_split = data2[0].split(' ') #removing the spaces

    #address = data_split[0]
    address = hex2dec(address)

    binary_rep1 = binary_repr(address, width = 16)
    print("binary num",binary_rep1)
    length = len(binary_rep1)
    print("length",length)

    polarity[i] = (address & polMask)

    #print("datasplit0 \n", data_split)
    if polarity[i] == 0:
        xOff[i] = (address & xMask)
        xOff[i] = xOff[i] >> xShift
        yOff[i] = (address & yMask)
        yOff[i] = yOff[i] >> yShift
    else:
        xOn[i] = (address & xMask)
        xOn[i] = xOn[i] >> xShift
        yOn[i] = (address & yMask)
        yOn[i] = yOn[i] >> yShift

    #rasterAddr[i] = x[i]*128+y[i]
    #print('rasteraddr',rasterAddr[i])
    # binary_rep = bin(rasterAddr[i])
    # print("binary",binary_rep)


    #for l in range(0,length)

#timestamp
    timestamp[i] = hex2dec(data_split[1])




#plt.plot(timestamp-timestamp[0], rasterAddr, 'bo')

plt.plot((timestamp-timestamp[0])/1000000, xOn*128+yOn, 'bo')
plt.plot((timestamp-timestamp[0])/1000000, xOff*128+yOff, 'ro')
plt.title('Raster plot for 20 Hz')
plt.xlabel('Time [sec]')
plt.ylabel('Address')
plt.show(block = False)
#plt.savefig('Green Led_20Hz')
time.sleep(30)

#save("signal", ext="png", close=True, verbose=True)
