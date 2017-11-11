#!/usr/bin/python
import os, time

mainDir = '/proj/MobilityFirst/ayadavDir'

cmd = mainDir+'/contextServiceScripts/KillProcesses.py'
os.system(cmd)
print "Java and hyperdex killed"


#os.system(mainDir+'/contextServiceScripts/CreateDir.py')