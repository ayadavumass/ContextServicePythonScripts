#!/usr/bin/python

import os, sys

numNodes = int(sys.argv[1])
print "numNodes" + str(numNodes)

# generate nodeList.txt
            
writef = open("nodeList.txt", "w")

curr = 0
while( curr < numNodes ):
    cmd = "ssh serv"+str(curr)+"\'hostname\'"
    os.system(cmd)
    curr = curr + 1
writef.close()