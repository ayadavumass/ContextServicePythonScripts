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

for index in range(len(lines)):
    print "Setting up gns account on "+str(lines[index])
    cmd = '/Users/ayadav/Documents/GNS/ContextServiceExpScripts/setupGNSCLI.sh '+str(lines[index])
    os.system(cmd)