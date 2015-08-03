__author__ = 'icub'
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

data = open("cd /dev/neuelab",'r+');
#biaswriter = open("/home/icub/Desktop/convertedbiases.txt",'w+');
#data = open("/home/icub/Desktop/biasesworkingfornewsetup",'r+');
biaswriter = open("/home/icub/Desktop/dump.txt",'w+');

'''
while True:
    c = data.read(1)
    if not c:
        break
    print c,
'''
for line in data:
    temp = line.split()
    print temp

    biaswriter.write(str(temp[0])+" "+ str(temp[1])+"\n")


data.close()