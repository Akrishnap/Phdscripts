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
import csv

#txt_file = r"/home/icub/Desktop/Ash/1hzdarkshuduse.txt"
#csv_file = r"/home/icub/Desktop/Ash/1hz.csv"

# use 'with' if the program isn't going to immediately terminate
# so you don't leave files open
# the 'b' is necessary on Windows
# it prevents \x1a, Ctrl-z, from ending the stream prematurely
# and also stops Python converting to / from different line terminators
# On other platforms, it has no effect
#in_txt = csv.reader(open(txt_file, "rb"), delimiter = ',')
#out_csv = csv.writer(open(csv_file, 'wb'))

#out_csv.writerows(in_txt)

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

rtext = readfile('/home/icub/Desktop/working/officelight/1hzworkingofficelightc1onc2off.txt', 0)
#rtext = readfile('/home/icub/Documents/Phd/research/lab/Aishwarya/vnt/greenledwoutlight/2hz/dump.txt', 0)
#rtext = readfile('/home/icub/Documents/Phd/lab/Aishwarya/vnt/greenledwoutlight/3hz/dump.txt', 0)
#rtext = readfile('/home/icub/Documents/Phd/lab/Aishwarya/vnt/greenledwoutlight/4hz/dump.txt', 0)
#rtext = readfile('/home/icub/Documents/Phd/lab/Aishwarya/vnt/greenledwoutlight/5hz/dump.txt', 0)
#rtext = readfile('/home/icub/Documents/Phd/lab/Aishwarya/vnt/greenledwoutlight/8.txt', 0)
#rtext = readfile('/home/icub/Documents/Phd/lab/Aishwarya/vnt/greenledwoutlight/10.txt', 0)
#rtext = readfile('/home/icub/Documents/Phd/lab/Aishwarya/vnt/greenledwoutlight/20.txt', 0)
size = len(rtext)
print ("data length", size)

#Initialisation
# sizeYRaster = 144 * 72 * 12 * 2
# sizeXRaster = 144 * 72 * 12 * 2

timestamp = zeros(size,int)

xOn = zeros(size, int)
yOn = zeros(size, int)
xOff = zeros(size, int)
yOff = zeros(size, int)

polarity = zeros(size, int)

rasterAddr = zeros(size, int)


for i in range(0,size): #doing for loop until the size of the data
    data2 = rtext[i].rsplit("\n") #splitting the data
    data_split = data2[0].split(' ')  #removing the spaces

    #print("values \n",values[-1])
    #print("length \n",len(data_split))
    if len(data_split) > 3:
            del(data_split[0])
            del(data_split[0])
    else:
            del(data_split[0])
    #print("final \n",data_split[-1])
    address = data_split[1]
    address = hex2dec(address)
    #print("dec \n",address)
    binary_rep1 = binary_repr(address, width = 16)
    #print("binary num",binary_rep1)
    length = len(binary_rep1)
    #print("length",length)

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

#timestamp
    timestamp[i] = hex2dec(data_split[1])

'''for subplot to split
plt.subplot(211)
plt.plot((timestamp)/10000000, xOn*128+yOn, 'bo',label= "ON Event")
plt.xlim(0,50)

plt.subplot(212)
plt.plot((timestamp)/10000000, xOn*128+yOn, 'bo',label= "ON Event")
plt.xlim(300,450)
#plt.axis([200,300,0,18000])
#plt.plot((timestamp)/10000000, xOff*128+yOff, 'ro',label = "OFF Event")
'''

plt.plot((timestamp)/10000000, xOn*128+yOn, 'bo',label= "ON Event")
#plt.xlim(90,180)
plt.legend(loc='upper left')
plt.title('Raster plot for 1hzworkingofficelightc1onc2off')
plt.xlabel('Time [1e-7sec]')
plt.ylabel('Address')
plt.show(block = False)
plt.savefig('1hzworkingofficelightc1onc2off')
time.sleep(30)

#save("signal", ext="png", close=True, verbose=True)
