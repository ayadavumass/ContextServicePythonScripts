# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#!/usr/bin/python
import os, sys

#myList = []
#f = open("workingPlanetlab40.txt","r") #opens file with name of "test.txt"
#myList = f.readlines()

lines = [line.strip() for line in open("relayNodeList2.txt")]

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
    
    #cmd = "ssh -oStrictHostKeyChecking=no -oConnectTimeout=5 -i /home/adipc/privatekey/planetlabKey umass_nameservice@"+lines[index]+" 'hostname'"
    #print cmd
    #node = lines[index].split( )
    #print node[1]
    #print "Starting context service on "+node[1]
    #cmd = '/home/ayadav/runContextService.sh '+node[1]+' '+str(node[0]) + ' '+str(sys.argv[1]) + ' ' + str(100)
    print "Node "+lines[index]
    #cmd = "ssh -oStrictHostKeyChecking=no -oConnectTimeout=5 -i /home/adipc/privatekey/planetlabKey umass_nameservice@"+lines[index]+" 'java -version'"
    #os.system(cmd)
    #print "\n\n"
    

writef = open("relayNodeConfig.txt", "w")

nodeID = 0
portStart = 7000

for index in range(len(lines)):
    writeStr = str(nodeID)+","+lines[index]+","+str(portStart)+"\n"
    nodeID = nodeID + 1
    portStart = portStart + 1
    writef.write(writeStr)
    
writef.close()