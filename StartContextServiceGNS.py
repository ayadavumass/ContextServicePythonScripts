#!/usr/bin/python
import os

lines = [line.strip() for line in open("contextServiceNodeSetup.txt")]

for index in range(len(lines)):
    node = lines[index].split( )
    print node[1]
    print "Starting context service on "+node[1]
    cmd = 'runContextService.sh '+str(node[0])
    os.system(cmd)