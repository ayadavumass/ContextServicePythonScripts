#!/bin/python

NumNodes = 12

writef = open("ns_hosts.txt", "w")

curr = 0
ipLastNum = 2
while(curr < NumNodes):
    nodeId = curr
    nodeName = "serv"+str(nodeId)
    nodeIP = "10.1.1."+str(ipLastNum)
    writeStr = str(nodeId)+" "+str(nodeName)+" "+str(nodeIP)+"\n"
    
    writef.write(writeStr)
    
    ipLastNum = ipLastNum + 1
    curr = curr + 1
    
writef.close()