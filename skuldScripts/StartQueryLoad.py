#!/usr/bin/python
import os, sys

scheme = sys.argv[1]
updateInterval = sys.argv[2]
queryInterval = sys.argv[3]

print "scheme running "+str(scheme)+" updateInterval "+str(updateInterval)+" queryInterval "+queryInterval

#lines = [line.strip() for line in open("100nodesSetup.txt")]
lines = ['compute-0-24']

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
    print "Starting query load on "+lines[index]
    for progID in range(0, 1):
        cmd = '/home/ayadav/runQueryLoad.sh '+lines[index]+' '+str(progID) + ' '+str(scheme) + ' '+str(updateInterval) 
        +' '+str(queryInterval) +' '+str(100)
        os.system(cmd)