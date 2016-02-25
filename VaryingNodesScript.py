#!/usr/bin/python
import os, sys, math, random
#from random import randint

def create_subspace_info(numNodes):
    N       = float(numNodes)
    Aavg    = 4.0
    B       = 12.0
    H       = 3.0
    P       = 2.0
    
    #writing the partition info file
    nodeID1                 = 0
    attributeNum            = 0

    numSubspaces            = B/H
    numNodesPerSubspace     = math.pow(P, H)
    i = 0

    writef1 = open("subspaceInfo.txt", "w")

    #writef2 = open("subspaceAttributes.txt", "w")

    while( i < numSubspaces ):
        pinfo = str(i)
        #nodeList = random.sample(xrange(int(numNodes)), int(numNodesPerSubspace))
        #nodeList.sort()
        
        currNodes = 0
        while( currNodes < numNodesPerSubspace ):
            pinfo = pinfo+","+str(nodeID1%numNodes)
            nodeID1 = nodeID1 + 1 
            currNodes = currNodes + 1
        
        #for nodeId in nodeList:
        #    pinfo = pinfo+","+str(nodeId)
        pinfo = pinfo + "\n"
        writef1.write(pinfo)

        k = 0
        attrInfo = str(i)
        while( k < H ):
            attrInfo = attrInfo + ", contextATT"+str(attributeNum)
            k = k + 1
            attributeNum = attributeNum + 1
        attrInfo = attrInfo + "\n"
        writef1.write(attrInfo)

        i = i + 1
    writef1.close()


contextServicePortNumStart  = 8000
dbPortNumStart              = 6000


numNodes = int(sys.argv[1])
print "numNodes" + str(numNodes)

# generate nodeList.txt

writef = open("nodeList.txt", "w")

curr = 0
while( curr < numNodes ):
    writeStr = "serv"+str(curr)+"\n"
    writef.write(writeStr)
    curr = curr + 1

writef.close()


# generate contextServiceNodeSetup.txt

writef = open("contextServiceNodeSetup.txt", "w")

curr = 0

while(curr < numNodes):
    currPortNum = contextServicePortNumStart + curr
    writeStr = str(curr)+" "+"serv"+str(curr)+" "+str(currPortNum)+"\n"
    writef.write(writeStr)
    curr = curr +1
writef.close()


# generate dbSetup.txt

writef = open("dbNodeSetup.txt", "w")

curr = 0
while(curr < numNodes):
    currPortNum = dbPortNumStart + curr
    writeStr = str(curr)+" "+"mysqlDir-serv"+str(curr)+" "+str(currPortNum)+"\n"
    writef.write(writeStr)
    curr = curr +1
writef.close()


# generate subspaceInfo.txt
create_subspace_info(numNodes)