#!/usr/bin/python
#$Id$
import numpy as np

def makeNorm(confFile):
    conf = __import__(confFile)
    reload(conf)
    f = open(conf.dataFile, 'r')
    f.readline() #sentinal line
    header = f.readline()
    column = header.split('\t')
    solventBL = np.array(range(conf.solvI,conf.solvF,conf.interval))
    solventBL /= conf.interval
    darkBL= np.array(range(conf.darkI,conf.darkF,conf.interval))
    darkBL /= conf.interval
    tolueneBL = np.array(range(conf.tolI,conf.tolF,conf.interval))
    tolueneBL /= conf.interval
    points = max(conf.solvF, conf.darkF, conf.tolF)
    points /= conf.interval
    data = readData(f, column, points)
    f.close()
    dark, darkPM, toluene, toluenePM, solvent, solventPM = getNorm(darkBL, solventBL, tolueneBL, data)
    output(conf.outFile, dark, toluene, solvent)
    return

def getNorm(darkBL, solventBL, tolueneBL, data):
    dark = data[darkBL,:].mean(0)
    darkPM = data[darkBL,:].std(0)
    toluene = data[tolueneBL,:].mean(0)
    toluenePM = data[tolueneBL,:].std(0)
    solvent = data[solventBL,:].mean(0)
    solventPM = data[solventBL,:].std(0)
    return dark, darkPM, toluene, toluenePM, solvent, solventPM

def output(outFile, dark, toluene, solvent):
    out = open(outFile,'w')
    out.write('import numpy as np')
    out.write('\n')
    out.write('dark = np.' + repr(dark) + '\n')
    out.write('\n')
    #out.write('darkBL = ' + str(darkPM) + '\n')
    out.write('toluene = np.' + repr(toluene) + '\n')
    out.write('\n')
    #out.write('tolueneBL = ' + str(toluenePM) + '\n')
    out.write('solvent = np.' + repr(solvent) + '\n')
    out.write('\n')
    #out.write('solventBL = ' + str(solventPM) + '\n')
    out.close()
    return

def readData(f, column, points):
    data = np.empty([points, column.__len__()-1])
    for i in range(points):
        data[i,:] = f.readline().split('\t')
    return data
