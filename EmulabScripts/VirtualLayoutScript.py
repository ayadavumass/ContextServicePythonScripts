#!/bin/python
import os

NumNodes = 100
clusterName = "d430"
imageName = "Ubuntu1604VirtualVM"
#imageName = "Ubuntu1404VirtualVM"
#imageName = "UBUNTU16-64-STD"


writef = open("emulabNodeSetupTcl.tcl", "w")

writeStr = "set ns [new Simulator]"+"\n"
writef.write(writeStr)


writeStr = "source tb_compat.tcl"+"\n"
writef.write(writeStr)


writeStr = "tb-set-vlink-emulation \"vlan\""+"\n"
writef.write(writeStr)


curr = 0
while(curr < NumNodes):
    writeStr = "set serv"+str(curr)+" [$ns node]"+"\n"
    writef.write(writeStr)
    
    writeStr = "tb-set-node-os $serv"+str(curr)+"  "+imageName+"\n"
    writef.write(writeStr)
    
    
    writeStr = "tb-set-hardware $serv"+str(curr)+" "+clusterName+"-vm"+"\n"
    writef.write(writeStr)
    
    
    writeStr = "tb-set-node-failure-action $serv"+str(curr)+"  "+"\"nonfatal\""+"\n"
    writef.write(writeStr)
    #tb-set-node-memory-size $node0 2048
    
    writeStr = "tb-set-node-memory-size $serv"+str(curr)+" "+"8192"+"\n"
    writef.write(writeStr)
    
    #$mynode add-attribute XEN_CORES YY 
    
    writeStr = "$serv"+str(curr)+" add-attribute XEN_CORES 4"+"\n"
    writef.write(writeStr)
    
    curr = curr + 1


curr = 0
writeStr = "set lan0 [$ns make-lan \""
while(curr < NumNodes):
    if(curr == 0):
        writeStr = writeStr + "$serv"+str(curr)
    else:
        writeStr = writeStr + " $serv"+str(curr)
        
    curr = curr + 1

writeStr = writeStr + "\"  100Mbps 0ms]"+"\n"
writef.write(writeStr)

writeStr = "tb-set-colocate-factor 6"+"\n"
writef.write(writeStr)

writeStr = "$ns run"+"\n"
writef.write(writeStr)
writef.close()