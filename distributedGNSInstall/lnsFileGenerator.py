#!/bin/python

NumNodes = 12

writef = open("lns_hosts.txt", "w")

curr = 0
while(curr < NumNodes):
    nodeId   = curr
    nodeName = "serv"+str(nodeId)
    writeStr = str(nodeName)+"\n"
    
    writef.write(writeStr)
    
    curr = curr + 1
    
writef.close()