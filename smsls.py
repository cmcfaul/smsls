#!/usr/bin/python
#$Id$
from numpy import *

datadir = 'C:\\Users\\cmcfaul\\Documents\\Data\\2013-03-25\\'
basename = 'c121031_stab_rev'
#setup the array to hold the pixels we want to keep
step = 3
cell_center = array ([20, 89, 155, 221, 285, 351, 418, 486])
range = step*arange(-5, 6, 1)
rangex,cellx = ix_(range, cell_center)
pixels = rangex+cellx

tempfile = open(datadir + basename + '_temperatures.txt')
tempfile.readline() #header size
tempfile.readline() #version
header = tempfile.readline() #sampling interval
interval = int(header.split(':')[1])
tempfile.readline() #sampling rate
tempfile.readline() #sample count
tempfile.readline() #device serial number
tempfile.readline() #column titles

datafile = open(datadir + basename + '_01.txt')
datafile.readline() #sentinal line

header = datafile.readline() #column titles
column = header.split('\t')
for i in arange(8):
	g = open(datadir + basename + '_c0' + str(i+1) + '.txt', 'w')
	g.write('Time (s), Temperature (C), ' , )
	for idx in pixels[:,0]:
		g.write( str(column[idx+1]) + ', ', )
	g.write('\n')
	for line in iter(datafile):
		#data = datafile.readline()
		ls = line.split('\t')
		data = tempfile.readline()
		temp = data.split(',')
		g.write(str(ls[0]) + ', ' , )
		g.write(str(temp[i+2]) + ', ' , )
		for idx in pixels[:,0]:
			g.write(str(ls[idx+1]) + ', ' , )
		g.write('\n')
	g.close
	print 'file ' + str(i) + ' is done.'
	
tempfile.close
datafile.close
