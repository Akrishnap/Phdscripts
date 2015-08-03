__author__ = 'icub'
#import pyNCS as p
import numpy
import string
import os
import random
import sys
import numpy
import getopt
import matplotlib.pyplot as plt
import array
import pylab
import matplotlib
import time
import math
import subprocess

#vnt_z2n = pyNCS.Chip('/home/icub/VNT/vnt.csv',id='vnt',amdaid='211')
portname = {'PrAdap' : 27,
            'ArbPd'  : 35,
            'TdRf' : 33,
            'SpOff' : 30,
            'SpDiff' : 32,
            'TdOn' : 22,
            'FollBias' : 44,
            'PrP' : 25,
            'ReqPuX' : 34,
            'ReqPuY' : 36,
            'SpRf' : 28,
            'TdOff' : 21,
            'Tdp' : 23,
            'PrCas' : 26,
            'PrSf' : 24,
            'SpOffThr' : 29,
            'SpOnThr' : 31};


biasname = sys.argv[1]
biasvalue = sys.argv[2]


#biasname='FollBias'
#biasvalue = str(0.3)
portnumber = portname.get(biasname)
#print portnumber

temp = float(biasvalue)*(65535/3.3)
temp = int(math.ceil(temp*100)/100)
temp=str(temp)

toExec = str("echo " +str(temp)+ " > out_voltage"+str(portnumber)+"_raw")
print toExec

subprocess.Popen(toExec,shell=True)
'''
data = open("/home/icub/Desktop/biases/vnt.biasesthatweshoulduse",'r+');
for line in range(0,16):                #considering all the lines as we have 17 lines
    temp =data.readline()
    print temp
'''
