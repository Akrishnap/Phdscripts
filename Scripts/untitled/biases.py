#from __future__ import print_function
import pyNCS as p
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

#print portname;
data = open("/home/icub/Desktop/biasesworkingfornewsetup",'r+');
biaswriter = open("/home/icub/Desktop/convertedbiases.txt",'w+');
scriptwriter = open("/home/icub/Desktop/biasesworkingfornewsetup.sh",'w+')
scriptwriter.write("#!/bin/bash \n")
scriptwriter.write("cd /sys/bus/iio/devices/iio:device1 \n")



#size = len(data)
for line in range(0,17):                #considering all the lines as we have 17 lines
    temp =data.readline().split();      # reading a single line and splitting
    #print temp                          #printing line by line after splitting
    #print temp[1]                          # printing the bias values
    temp[0] = str(temp[0])   # printing the bias names
    #print temp[0]
    temp[1] = float(temp[1])*(65535/3.3)       # when the lines are splitted, it converts the bias values into string
                                               # so cannot calculate. should convert to float
    #print temp[1]
    #print int(math.ceil(temp[1]*100)/100)
    temp[1] =  int(math.ceil(temp[1]*100)/100)   # in order to round off the value and to have the integer value
    #print temp[1]

    biaswriter.write(temp[0]);
    biaswriter.write(" ");
    biaswriter.write(str(temp[1]));
    #biaswriter.writelines(str(temp))
    biaswriter.writelines(str('\n'))
    #it = portname.get(temp[0])
    portnumber =portname.get(temp[0])
    #print it
    print portnumber
    '''
    scriptwriter.write("echo")
    scriptwriter.write(" ");
    scriptwriter.write(str(temp[1]));
    scriptwriter.write(" ");
    scriptwriter.write("> out_voltage")
    scriptwriter.write(str(portnumber))
    scriptwriter.write("_raw ")
    scriptwriter.writelines(str('\n'))
    '''
    scriptwriter.write("echo "+str(temp[1])+" >out_voltage"+str(portnumber)+"_raw"+"\n")
    #eval("echo "+str(temp[1])+" >out_voltage"+str(portnumber)+"_raw"+"\n")
data.close();
biaswriter.close();
scriptwriter.close();



