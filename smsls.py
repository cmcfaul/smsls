#!/usr/bin/python
#$Id$
from numpy import *

datadir = 'C:\\Users\\cmcfaul\\Documents\\Data\\'
datedir = raw_input('Enter the date of the data (in yyyy-mm-dd) ')
basename = raw_input('What is the basename of the file? ') #'c121031_stab_rev'
outFile = []
for i in arange(8):
	f = open(datadir + datedir + '\\' + basename + '_c0' + str(i+1) + '.dat', 'w')
	outFile.append(f)

#setup the array to hold the pixels we want to keep
step = 3
cell_center = array ([20, 89, 155, 221, 285, 351, 418, 486])
cell_range = step*arange(-5, 6, 1)
rangex,cellx = ix_(cell_range, cell_center)
pixels = rangex+cellx

tempfile = open(datadir + datedir + '\\' + basename + '_temperatures.txt')
tempfile.readline() #header size
tempfile.readline() #version
header = tempfile.readline() #sampling interval
interval = int(header.split(':')[1])
tempfile.readline() #sampling rate
tempfile.readline() #sample count
tempfile.readline() #device serial number
tempfile.readline() #column titles

datafile = open(datadir + datedir + '\\' + basename + '.txt')
datafile.readline() #sentinal line

header = datafile.readline() #column titles
column = header.split('\t')
for i in arange(8):
	outFile[i].write('Time (s), Temperature (C), ' , )
	for idx in pixels[:,i]:
		outFile[i].write( str(column[idx+1]) + ', ', )
	outFile[i].write('\n')
for line in iter(datafile):
	ls = line.split('\t')
	data = tempfile.readline()
	temp = data.split(',')
	for i in arange(8):
		outFile[i].write(str(ls[0]) + ', ' , )
		outFile[i].write(str(temp[i+2]) + ', ' , )
		for idx in pixels[:,i]:
			outFile[i].write(str(ls[idx+1]) + ', ' , )
		outFile[i].write('\n')
for i in arange(8):
	outFile[i].close()
	
tempfile.close()
datafile.close()
