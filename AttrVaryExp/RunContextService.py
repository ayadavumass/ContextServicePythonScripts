#!/usr/bin/python
import os, sys

#myList = []
#f = open("workingPlanetlab40.txt","r") #opens file with name of "test.txt"
#myList = f.readlines()
print "scheme running "+sys.argv[1]

scheme = sys.argv[1]
numAttr = sys.argv[2]


lines = [line.strip() for line in open("100nodesSetup.txt")]

#print(lines)
#for line in f:
#    myList.append(str(line))

#f.close()
# don't need to copy each time
#cmd = 'bash /Users/ayadav/Documents/GNS/ContextServiceExpScripts/scpContextServiceParallel.sh'
#os.system(cmd)

#cmd = 'bash /Users/ayadav/Documents/GNS/ContextServiceExpScripts/runContextServiceParallel.sh'
#os.system(cmd)
for index in range(len(lines)):
    node = lines[index].split( )
    print node[1]
    print "Starting context service on "+node[1]
    cmd = '/home/ayadav/runContextService.sh '+node[1]+' '+str(node[0]) + ' '+str(sys.argv[1])+' '+str(numAttr)
    os.system(cmd)