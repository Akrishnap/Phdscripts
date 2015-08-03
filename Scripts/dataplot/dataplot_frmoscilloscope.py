__author__ = 'icub'
import matplotlib.pyplot as plt
import matplotlib
import numpy
from pylab import *
from matplotlib  import *
from matplotlib import rc
import pylab as pl
import csv
import time
import math

with open('/home/icub/Desktop/data/data.csv') as csvfile:
    i = 1
    x = []
    y = []


    for line in csvfile:
        splitline=line.split()
        x.append(splitline[0])
        y.append(splitline[1])

    #result = [i*z for i in x]
    plt.plot(x, y,'r')
    plt.show()
    csvfile.close()
    plt.xlabel('Time[us]')
    plt.ylabel('Amplitude')
    #plt.text()
