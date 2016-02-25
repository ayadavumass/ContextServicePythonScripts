#!/usr/bin/python
import os
#mainDir="/proj/MobilityFirst/ayadavDir"
#myList = []
#f = open("workingPlanetlab40.txt","r") #opens file with name of "test.txt"
#myList = f.readlines()

lines = [line.strip() for line in open("nodeList.txt")]
print(lines)
#for line in f:
#    myList.append(str(line))
#f.close()

for index in range(len(lines)):
    print "Killing java on "+lines[index]
    cmd = './killAll.sh '+lines[index]
    os.system(cmd)


    print "Dropping mongo on "+lines[index]
    cmd = './mongoDrop.sh '+lines[index]
    os.system(cmd)