#!/bin/python
import os

NumNodes = 12
clusterName = "d710"
imageName = "UbuntuJava-Mongo-SQL"
#imageName = "UBUNTU16-64-STD"


writef = open("emulabNodeSetupTcl.tcl", "w")

writeStr = "set ns [new Simulator]"+"\n"
writef.write(writeStr)

writeStr = "source tb_compat.tcl"+"\n"
writef.write(writeStr)

curr = 0
while(curr < NumNodes):
    writeStr = "set node"+str(curr)+" [$ns node]"+"\n"
    writef.write(writeStr)
    
    writeStr = "tb-set-hardware $node"+str(curr)+" "+"pcvm"+"\n"
    writef.write(writeStr)
    
    writeStr = "tb-set-node-os $node"+str(curr)+"  "+"OPENVZ-STD"+"\n"
    writef.write(writeStr)
    
    writeStr = "tb-set-node-failure-action $node"+str(curr)+"  "+"nonfatal"+"\n"
    writef.write(writeStr)
    
    curr = curr + 1
    
curr = 0
writeStr = "set lan0 [$ns make-lan \""
while(curr < NumNodes):
    if(curr == 0):
        writeStr = writeStr + "$node"+str(curr)
    else:
        writeStr = writeStr + " $node"+str(curr)
        
    curr = curr + 1

writeStr = writeStr + "\"  100Mbps 0ms]"+"\n"
writef.write(writeStr)

writeStr = "tb-set-colocate-factor 4"+"\n"
writef.write(writeStr)

writeStr = "$ns run"+"\n"
writef.write(writeStr)
writef.close()