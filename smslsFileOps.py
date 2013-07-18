#!/usr/bin/python
#$Id: $
import numpy as np

def main(*arg):
	if arg:
		baseName = arg[0]
		mode = arg[1]
	else:
		baseName = raw_input('What is the basename of the file? ') 
		mode = raw_input('Do you want peaks or rolloff? ')
	outFile = createOutFiles(baseName)
	pixels = getWhichPixels(mode)
	haveTemperatures = raw_input('Do you have a temperature file? ')
	if haveTemperatures in ['1', 'y', 'yes' 'Yes' 'YES', 'True']:
		tempFile = baseName + '_temperatures.txt'
		f, header, column = readTempHeader(tempFile)
		writeOut(baseName, f, pixels, outFile)
	else:
		writeOut(baseName, 'none', pixels, outFile)
	return

def createOutFiles(baseName):
	outFile = []
	for i in range(8):
		f = open(baseName+'_c'+str(i+1)+'.dat', 'w')
		outFile.append(f)
	return outFile

def getWhichPixels(mode):
	#setup the array to hold the pixels we want to keep
	cell_center = np.array ([20, 89, 155, 221, 285, 351, 418, 486])
	if mode == 'peaks':
		pixels = cell_center
	elif mode == 'rolloff':
		step = 3
		cell_range = step*np.arange(-5, 6, 1)
		rangex,cellx = np.ix_(cell_range, cell_center)
		pixels = rangex+cellx
	return pixels

def readTempHeader(tempFile):
	f = open(tempFile, 'r')
	header = {}
	for i in range(6):
		line = f.readline() 
		param, value = line.split(':')
		header[param] = value
	period = int(header['Sampling Interval'])
	freq = int(header['Sampling Rate'])
	points = int(header['Sample Count'])
	column = f.readline().split(',') #column titles
	#leave f open, and return a file object
	return f, header, column

def writeOut(baseName, tempfile, pixels, outFile):
	datafile = open(baseName+'.txt')
	datafile.readline() #sentinal line
	header = datafile.readline() #column titles
	column = header.split('\t')
	temp = hasattr(tempfile, 'readline')
	for i in range(8):
		outFile[i].write('Time (s), ' , )
		if temp:
			outFile[i].write('Temperature (C), ' , )
		if pixels.shape[0] != 8:
			for idx in pixels[:,i]:
				outFile[i].write( str(column[idx+1]) + ', ', )
		else:
			outFile[i].write( str(column[pixels[i]+1]) + ', ', )
		outFile[i].write('\n')
	for line in iter(datafile):
		ls = line.split('\t')
		if temp:
			data = tempfile.readline()
			temperature = data.split(',')
		for i in range(8):
			outFile[i].write(str(ls[0]) + ', ' , )
			if temp:
				outFile[i].write(str(temperature[i+2]) + ', ' , )
			if pixels.shape[0] != 8:
				for idx in pixels[:,i]:
					outFile[i].write(str(ls[idx+1]) + ', ' , )
			else:
				outFile[i].write( str(ls[pixels[i]+1]) + ', ', )
			outFile[i].write('\n')
	for i in range(8):
		outFile[i].close()
	if temp:
		tempfile.close()
	datafile.close()
	return