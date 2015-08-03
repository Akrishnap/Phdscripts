__author__ = 'icub'
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

writer = open("/home/icub/Desktop/biases.txt",'w+')
'''
biasname = sys.argv[1]
biasvalue = sys.argv[2]
'''

biasname='FollBias'
biasvalue = str(0.3)

portnumber = portname.get(biasname)
print portnumber
writer.write(biasname)
writer.write(" ")
writer.write(biasvalue)
writer.write("\n")

