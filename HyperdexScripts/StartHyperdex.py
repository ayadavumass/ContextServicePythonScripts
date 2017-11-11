#!/usr/bin/python
import os, sys

#myList = []
#f = open("workingPlanetlab40.txt","r") #opens file with name of "test.txt"
#myList = f.readlines()
#print "scheme running "+sys.argv[1]

lines = [line.strip() for line in open("/proj/MobilityFirst/ayadavDir/experimentScripts/topologySetup.txt")]

#print(lines)
#for line in f:
#    myList.append(str(line))

#f.close()
# don't need to copy each time
#cmd = 'bash /Users/ayadav/Documents/GNS/ContextServiceExpScripts/scpContextServiceParallel.sh'
#os.system(cmd)

# start the coordinator
cmd = '/proj/MobilityFirst/ayadavDir/experimentScripts/runHyperdexCoord.sh serv0'
os.system(cmd)

time.sleep(10)

#cmd = 'bash /Users/ayadav/Documents/GNS/ContextServiceExpScripts/runContextServiceParallel.sh'
#os.system(cmd)
for index in range(len(lines)):
    node = lines[index].split( )
    print node[1]
    print "Starting hyperdex on "+node[1]
    cmd = '/proj/MobilityFirst/ayadavDir/experimentScripts/runHyperdexDaemon.sh '+node[1]+' '+str(node[2]) + ' '+str(node[0])
    os.system(cmd)
    
time.sleep(10)

print "all daemon started"
cmd = '/proj/MobilityFirst/ayadavDir/experimentScripts/contextspace.sh'
os.system(cmd)

print "context space created"