# -*- coding: utf-8 -*-
import os
import json
import pickle
from numpy import *

f = open('/home/icub/Desktop/sinewave3.3square/30hz.txt','r')
#x = json.load(f)
#json.dump(x, f)

#Results = pickle.load(f)
#print('Res \n', Results)

lines = f.readlines()
try:
    json.loads(lines[-1])
except ValueError:
    with open('/home/icub/Desktop/sinewave3.3square/30h.txt', 'w') as f:
        f.write(''.join(lines[:-1]))

