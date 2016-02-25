#!/bin/python
import os
import time

#myList = []
#f = open("workingPlanetlab40.txt","r") #opens file with name of "test.txt"
#myList = f.readlines()

lines = [line.strip() for line in open("dummyContextValues.gcli")]

print(lines)
#for line in f:
#    myList.append(str(line))

#f.close()

for index in range(len(lines)):
    print "Updating "+lines[index]
    cmd = 'echo "'+lines[index]+'" | java -jar /Users/ayadav/gns-cli-1.12-2014-10-27.jar';
    #cmd = '/Users/ayadav/Documents/GNS/ContextServiceExpScripts/killAll.sh '+lines[index]
    os.system(cmd)
    time.sleep(5)