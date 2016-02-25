#!/bin/python
import os

NumNodes = 40
clusterName = "d710"
imageName = "UbuntuJava-Mongo-SQL"

writef = open("emulabNodeSetupTcl.tcl", "w")

writeStr = "set ns [new Simulator]"+"\n"
writef.write(writeStr)

writeStr = "source tb_compat.tcl"+"\n"
writef.write(writeStr)

curr = 0
while(curr < NumNodes):
    writeStr = "set serv"+str(curr)+" [$ns node]"+"\n"
    writef.write(writeStr)
    
    writeStr = "tb-set-hardware $serv"+str(curr)+" "+clusterName+"\n"
    writef.write(writeStr)
    
    writeStr = "tb-set-node-os $serv"+str(curr)+"  "+imageName+"\n"
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

writeStr = writeStr + "\"  1000Mbps 0ms]"+"\n"
writef.write(writeStr)

writeStr = "$ns run"+"\n"
writef.write(writeStr)
writef.close()