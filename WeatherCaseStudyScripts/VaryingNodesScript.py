#!/usr/bin/python
import os, sys, math, random

# config files are created are installed in this directory
#scriptOutputDir = "/proj/MobilityFirst/ayadavDir/ContextNetGitHub/contextnet/conf/emulabConf/contextServiceConf"
#homeDir = "/home"

contextServicePortNumStart  = 8000
dbPortNumStart              = 6000


numNodes            = int(sys.argv[1])
CSScriptOutputDir   = sys.argv[2]
homeDir             = sys.argv[3]
GNSScriptOutpurDir  = sys.argv[4]



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

writef = open(CSScriptOutputDir+"/contextServiceNodeSetup.txt", "w")

curr = 0

while(curr < numNodes):
    currPortNum = contextServicePortNumStart + curr
    writeStr = str(curr)+" "+"serv"+str(curr)+" "+str(currPortNum)+"\n"
    writef.write(writeStr)
    curr = curr +1
writef.close()


# generate dbSetup.txt
# nodeiD, portnum, databasename, username, password, arguments
#0 3306 contextDB0 root aditya
#1 3306 contextDB1 root aditya
#2 3306 contextDB2 root aditya
#3 3306 contextDB3 root aditya

writef = open(CSScriptOutputDir+"/dbNodeSetup.txt", "w")

writeStr = "# nodeiD, portnum, databasename, username, password, arguments \n"
writef.write(writeStr)

curr = 0
while(curr < numNodes):
    nodeId      = curr
    dirName     = "mysqlDir-serv"+str(nodeId)
    currPortNum = dbPortNumStart + nodeId
    dbName      = "contextDB"+str(nodeId)
    userName    = "root"
    password    = "aditya"
    arguments   = "socket="+homeDir+"/"+dirName+"/thesock"
    
    writeStr = str(curr)+" "+str(currPortNum)+" "+dbName+" "+userName+" "+password+" "+arguments+"\n"
    
    writef.write(writeStr)
    curr = curr + 1
writef.close()


#writing the partition info file
writef1 = open(CSScriptOutputDir+"/subspaceInfo.txt", "w")

i=0
#writef2 = open("subspaceAttributes.txt", "w")
pinfo = str(i)

currNodes = 0
while( currNodes < numNodes ):
    pinfo = pinfo+","+str(currNodes)
    currNodes = currNodes + 1

pinfo = pinfo + "\n"
writef1.write(pinfo)
writef1.write("0, geoLocationCurrentLat, geoLocationCurrentLong")

writef1.close()


# writing gns lns_hosts file
writef = open(GNSScriptOutpurDir+"/lns_hosts.txt", "w")

curr = 0
while(curr < numNodes):
    nodeId   = curr
    nodeName = "serv"+str(nodeId)
    writeStr = str(nodeName)+"\n"
    
    writef.write(writeStr)
    
    curr = curr + 1
    
writef.close()


# writing gns ns_hosts file
writef = open(GNSScriptOutpurDir+"/ns_hosts.txt", "w")

curr = 0
ipLastNum = 2
while(curr < numNodes):
    nodeId = curr
    nodeName = "serv"+str(nodeId)
    nodeIP = "10.1.1."+str(ipLastNum)
    writeStr = str(nodeId)+" "+str(nodeName)+" "+str(nodeIP)+"\n"
    
    writef.write(writeStr)
    
    ipLastNum = ipLastNum + 1
    curr = curr + 1
    
writef.close()


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

    writef1 = open(CSScriptOutputDir+"/subspaceInfo.txt", "w")

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