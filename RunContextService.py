#!/bin/python
import os

#myList = []
#f = open("workingPlanetlab40.txt","r") #opens file with name of "test.txt"
#myList = f.readlines()

lines = [line.strip() for line in open("contextServiceList.txt")]

print(lines)
#for line in f:
#    myList.append(str(line))

#f.close()
# don't need to copy each time
cmd = 'bash /Users/ayadav/Documents/GNS/ContextServiceExpScripts/scpContextServiceParallel.sh'
os.system(cmd)


cmd = 'bash /Users/ayadav/Documents/GNS/ContextServiceExpScripts/runContextServiceParallel.sh'
os.system(cmd)

#for index in range(len(lines)):
#    print "Starting context service on "+str(lines[index])
#    
#    cmd = '/Users/ayadav/Documents/GNS/ContextServiceExpScripts/runContextService.sh '+str(lines[index])
#    os.system(cmd)