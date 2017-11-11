#!/usr/bin/python
import os, sys

scheme = sys.argv[1]
updateInterval = sys.argv[2]
queryInterval = sys.argv[3]
attrNum = sys.argv[4]

print "scheme running "+str(scheme)+" updateInterval "+str(updateInterval)+" queryInterval "+queryInterval+" attrNum "+attrNum

#lines = [line.strip() for line in open("100nodesSetup.txt")]
lines = ['compute-0-23']

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
    print "Starting update load on "+lines[index]
    for progID in range(0, 5):
        cmd = '/home/ayadav/runUpdateLoad.sh '+lines[index]+' '+str(progID) + ' '+str(scheme) + ' '+str(updateInterval) +' '+str(queryInterval)+' '+str(attrNum)
        os.system(cmd)