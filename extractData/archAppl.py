# Author: K. Gofron
# Date: 2016-3-11
# This program extract single PV data from archiver appliance and wirtes them to a file
#

import sys, getopt
import numpy as np
from chaco.shell import *
import urllib2
import json
import pandas as pd

#temp
import matplotlib.pyplot as plt

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

PV = sys.argv[1]
outFile = sys.argv[2]
fromT = sys.argv[3]
toT = sys.argv[4]
archiverURL = "http://xf10id-ca1.cs.nsls2.local:17668/"
retreveURL = archiverURL + "retrieval/data/getData.json?pv=" + PV + "&from=" + fromT + "T00:00:00Z&to=" + toT + "T14:00:00Z"
print "The URL:", retreveURL

req = urllib2.urlopen(retreveURL)

# data has a type of "list" when loaded by json
data = json.load(req)


# lists of values, with index corresponding to one row.
sec = []
nanos = []
val = []


csvfile = open(outFile, 'wb')
csvfile.write('%s,%s,%s \n' % ('secs', 'nanos', 'val'))
for i in data[0]['data']:
    csvfile.write('%d,%d,%s\n' % (i['secs'], i['nanos'], i['val']))
    
    if i['val'] < 60 and i['val'] > 15:
        sec.append(i['secs'])
        nanos.append(i['nanos'])
        val.append(i['val'])
csvfile.close()


# plot data lists
plt.plot(sec, val, 'r-')
plt.xlabel('Seconds')
plt.ylabel('Values')
#plt.show() #if want to show

plt.savefig(outFile[:-4] + ".png")#, bbox_inches='tight')


"""
dataFile = open(outFile, 'r')
lst = []
for line in dataFile:
    data = line.split(",")
    lst.append(data)
dataFile.close()
x = linspace(lst[1][0], lst[(len(lst))-1][0], 100)
"""

# "{u'meta': {u'name': u'XF:10ID-BI{TM176}X-I', u'PREC': u'0'}, u'data': [{u'nanos': 212921852, u'status': 0, u'secs': 1457648711, u'severity': 0, u'val': 4.716684004584329}, {u'nanos': 320278264, u'status': 0, u'secs': 1457648711, u'severity': 0, u'val': 3.929288158031524},


