#!/usr/bin/python
#$Id$
from numpy import *

#setup the array to hold the pixels we want to keep
step = 3
cell_center = array ([20, 89, 155, 221, 285, 351, 418, 486])
range = step*arange(-5, 6, 1)
rangex,cellx = ix_(range, cell_center)
pixels = rangex+cellx

tempfile = open('c121031_stab_rev_temperatures.txt')
tempfile.readline() #header size
tempfile.readline() #version
header = tempfile.readline() #sampling interval
interval = int(header.split(':')[1]
tempfile.readline() #sampling rate
tempfile.readline() #sample count
tempfile.readline() #device serial number
tempfile.readline() #column titles

datafile = open('c121031_stab_rev_01.txt')
datafile.readline() #sentinal line
datafile.readline() #column titles

temp = tempfile.readline()
data = datafile.readline()
ls = data.split('\t')
for idx in pixels[:,0]
	print ls[idx]
	print ',' 
print '\n'

f.close
