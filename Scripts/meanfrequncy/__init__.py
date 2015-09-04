# -*- coding: utf-8 -*-
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

polMask = 1
xMask   = hex2dec("FE")
yMask   = hex2dec("7F00")
xShift  = 1
yShift  = 8

f1= readfile('/home/icub/Desktop/sinewave3.3square/1.txt',0)
f2= readfile('/home/icub/Desktop/sinewave3.3square/10.txt',0)
f3= readfile('/home/icub/Desktop/sinewave3.3square/30.txt',0)
f4= readfile('/home/icub/Desktop/sinewave3.3square/60.txt',0)
f5= readfile('/home/icub/Desktop/sinewave3.3square/90.txt',0)
f6= readfile('/home/icub/Desktop/sinewave3.3square/100.txt',0)

size = len(f1)
size1 = len(f2)
size2 = len(f3)
size3 = len(f4)
size4 = len(f5)
size5 = len(f6)

timestamp = zeros(size,int)
timestamp1 = zeros(size1,int)
timestamp2 = zeros(size2,int)
timestamp3 = zeros(size3,int)
timestamp4 = zeros(size4,int)
timestamp5 = zeros(size5,int)

frequency = [1,10,30,60,90,100]





for i in range(0,size): #doing for loop until the size of the data
    data2 = f1[i].rsplit("\n") #splitting the data
    data_split = data2[0].split()#removing the spaces
    timestamp[i] = hex2dec(data_split[1])
    a = 1./diff(timestamp)
    #a = (1/timestamp[i])
#print("t1 \n",timestamp)
#print("a \n",a)
#print("t2 \n",1/timestamp)
#print("mean \n", mean(timestamp))


#f = (1/timestamp)
out_freq1=mean(a)
mean1 = mean(timestamp)
stddev1 = std(timestamp)


for i in range(0,size1): #doing for loop until the size of the data
    data2 = f2[i].rsplit("\n") #splitting the data
    data_split = data2[0].split()#removing the spaces
    timestamp1[i] = hex2dec(data_split[1])
    a1 = 1./diff(timestamp1)
    #a1 = (1/timestamp1[i])
out_freq2 = mean(a1)
mean2 = mean(timestamp1)
stddev2 = std(timestamp1)


for i in range(0,size2): #doing for loop until the size of the data
    data2 = f3[i].rsplit("\n") #splitting the data
    data_split = data2[0].split()#removing the spaces
    timestamp2[i] = hex2dec(data_split[1])
    #a2 = (1/timestamp2[i])
    a2 = 1./diff(timestamp2)
out_freq3=mean(a2)
mean3 = mean(timestamp2)
stddev3 = std(timestamp2)



for i in range(0,size3): #doing for loop until the size of the data
    data2 = f4[i].rsplit("\n") #splitting the data
    data_split = data2[0].split()#removing the spaces
    timestamp3[i] = hex2dec(data_split[1])
    #out_freq4=np.mean(1/timestamp3[i])
    a3 = 1./diff(timestamp3)
out_freq4 = mean(a3)
mean4 = mean(timestamp3)
stddev4 = std(timestamp3)



for i in range(0,size4): #doing for loop until the size of the data
    data2 = f5[i].rsplit("\n") #splitting the data
    data_split = data2[0].split()#removing the spaces
    timestamp4[i] = hex2dec(data_split[1])
    #out_freq5=np.mean(1/timestamp4[i])
    a4 = 1./diff(timestamp4)
out_freq5 = mean(a4)
mean5 = mean(timestamp4)
stddev5 = std(timestamp4)


for i in range(0,size5): #doing for loop until the size of the data
    data2 = f6[i].rsplit("\n") #splitting the data
    data_split = data2[0].split()#removing the spaces
    timestamp5[i] = hex2dec(data_split[1])
    a5 = 1./diff(timestamp5)
out_freq6 = mean(a5)
mean6 = mean(timestamp5)
stddev6 = std(timestamp5)


global_timestamps = [timestamp,timestamp1,timestamp2,timestamp3,timestamp4,timestamp5]
print('timsg \n',global_timestamps[0])

for j in range(len(frequency)):
    #print('j\n',frequency[j])
    #print('jg\n',global_timestamps[j])
    plt.hold(True)
    for k in range(len(global_timestamps[j])):

        plt.hold(True)
        plt.subplot(3, 1,1)
        plt.plot((global_timestamps[j][k]),frequency[j],'ro--')

        #plt.ylabel('Frequency(Hz)')
        #plt.xlabel('Timestamps(us)')
        #plt.ylim(-5,110)
        #plt.hold(True)

#plt.savefig('singlepixelresponse2')
#plt.show()
#time.sleep(10)

In_frequency = [1,10,30,60,90,100]
#In_frequency = [1,10,100]
#Out_frequency = [out_freq1*100000,out_freq2*100000,out_freq3*100000,out_freq4*100000,out_freq5*100000]
#Out_frequency = [out_freq1*100000,out_freq2*100000,out_freq3*100000]
Out_frequency = [out_freq1,out_freq2,out_freq3,out_freq4,out_freq5,out_freq6]
Mean = [mean1,mean2,mean3,mean4,mean5,mean6]
Stddev = [stddev1,stddev2,stddev3,stddev4,stddev5,stddev6]

plt.subplot(3,1,2)
plt.plot(In_frequency,Out_frequency,marker='o', linestyle='--', color='r')
plt.ylabel('Output frequency(Hz)')
plt.xlabel('Input frequency(Hz)')
plt.subplot(3,1,3)
plt.plot(In_frequency,Mean,linestyle='--', color='m')
plt.hold(True)
plt.errorbar(In_frequency, Mean, Stddev, linestyle='None', marker='o')

#plt.ylim(0,5)
#plt.xlim(0,110)
#plt.ylim(3,110)
#plt.ylabel('Output frequency(Hz)')
#plt.xlabel('Input frequency(Hz)')
'''
plt.subplot(3,1,3)
plt.plot(In_frequency,Out_frequency,'ro')

#plt.ylim(0,5)
plt.xlim(0,110)
plt.ylim(3,11)
plt.ylabel('Output frequency(Hz)')
plt.xlabel('Input frequency(Hz)')
'''
plt.show(block = False)
plt.savefig('OutfreqvsInfreq1')
time.sleep(10)
