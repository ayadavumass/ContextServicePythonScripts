#!/usr/bin/python
import os

mainDir = "/proj/MobilityFirst/ayadavDir"
#myList = []
#f = open("workingPlanetlab40.txt","r") #opens file with name of "test.txt"
#myList = f.readlines()

lines = [line.strip() for line in open(mainDir+"/contextServiceScripts/contextServiceNodeSetup.txt")]

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
    node = lines[index].split( )
    print node[1]
    
    #print "Removing localDir on "+node[1]
    #cmd = '/home/ayadav/runContextService.sh '+node[1]+' '+str(node[0])    

    #cmd = 'rm -rf '+mainDir+'/contextServiceScripts/localDir-'+node[1]+'-'+str(node[0])
    #os.system(cmd)
    
    print "Creating localDir on "+node[1]

    cmd = mainDir+'/contextServiceScripts/createDir.sh '+str(node[0])+' '+str(node[1])
    os.system(cmd)
    
    #cmd = '/home/ayadav/runContextService.sh '+node[1]+' '+str(node[0])    

    #cmd = 'mkdir '+mainDir+'/contextServiceScripts/localDir-'+node[1]+'-'+str(node[0])
    #os.system(cmd)

    #cmd = 'cp -rf '+mainDir+'/contextServiceScripts/contextServiceNodeSetup.txt '+mainDir+'/contextServiceScripts/localDir-'+node[1]+'-'+str(node[0])
    #os.system(cmd)

    #cmd = 'cp -rf '+mainDir+'/contextServiceScripts/dbNodeSetup.txt '+mainDir+'/contextServiceScripts/localDir-'+node[1]+'-'+str(node[0])
    #os.system(cmd)

    #cmd = 'cp -rf '+mainDir+'/contextServiceScripts/subspaceInfo.txt '+mainDir+'/contextServiceScripts/localDir-'+node[1]+'-'+str(node[0])
    #os.system(cmd)

    #cmd = 'cp -rf '+mainDir+'/contextServiceScripts/contextServiceNodeSetup.txt '+mainDir+'/contextServiceScripts/requestOutput/.'
    #os.system(cmd)

print "Creating requestDir on serv32"

cmd = mainDir+'/contextServiceScripts/createDirReqLoad.sh serv32'
os.system(cmd)

cmd = mainDir+'/contextServiceScripts/createDirReqLoad.sh serv33'
os.system(cmd)

cmd = mainDir+'/contextServiceScripts/createDirReqLoad.sh serv34'
os.system(cmd)