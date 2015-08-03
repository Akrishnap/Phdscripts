from __future__ import print_function

__author__ = 'icub'
import numpy
import random
import os
import sys



pi_tuple=(1,2,3,4,5)

new_t = list(pi_tuple)
new_list = tuple(pi_tuple)

len(pi_tuple)

super_vi = {'sk': "Leo",
            'captain harry': "kris"}

print(super_vi['captain harry'])

del super_vi['sk']

super_vi['captain harry'] = 'Julia Roberts'

print(len(super_vi))

print(super_vi.get('captain harry'))

print(super_vi.keys())

print(super_vi.values())

for x in range(0,10):
    print(x,' ', end=" ")

print('\n')

#create and open a file and use ab+ to read and append the file
test_file=open("test.txt", "wb")

print(test_file.mode)

print(test_file.name)

test_file.write(bytes("sk be with me\n"))

test_file.close()

text_file = open("test.txt","r+")
print(text_file)

os.remove("test.txt")
