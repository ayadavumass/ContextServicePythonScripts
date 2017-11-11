
NumNodes = 4

writef = open("gnsserver.emulab.properties", "w")


writeStr = "IN_MEMORY_DB=false"+"\n"
writef.write(writeStr)

writeStr = "ENABLE_EMAIL_VERIFICATION=false"+"\n"
writef.write(writeStr)


writeStr = "ENABLE_DISKMAP=false"+"\n"
writef.write(writeStr)


writeStr = "CLIENT_SSL_MODE=SERVER_AUTH"+"\n"
writef.write(writeStr)


writeStr = "SERVER_SSL_MODE=MUTUAL_AUTH"+"\n"
writef.write(writeStr)


writeStr = "DEMAND_PROFILE_TYPE=edu.umass.cs.gnsserver.gnsapp.demandprofiles.SqrtNReplicationDemandProfile"+"\n"
writef.write(writeStr)


writeStr = "APPLICATION=edu.umass.cs.gnsserver.gnsapp.GNSApp"+"\n"
writef.write(writeStr)


curr = 0

while(curr < NumNodes):
    nodeId = curr
    nodeName = "serv"+str(nodeId)
    key="active.GNSApp"+str(NumNodes)+"."+str(nodeId)
    writeStr = key+"="+str(nodeName)+":24403"+"\n"
    
    writef.write(writeStr)
    
    
    key="reconfigurator.RC"+str(NumNodes)+"."+str(nodeId)
    writeStr = key+"="+str(nodeName)+":2178"+"\n"
    
    writef.write(writeStr)
    
    
    curr = curr + 1
    
    
writeStr = "-Djavax.net.ssl.keyStorePassword=qwerty"+"\n"
writef.write(writeStr)


writeStr = "-Djavax.net.ssl.keyStore=conf/keyStore/node100.jks"+"\n"
writef.write(writeStr)


writeStr = "-Djavax.net.ssl.trustStorePassword=qwerty"+"\n"
writef.write(writeStr)


writeStr = "-Djavax.net.ssl.trustStore=conf/keyStore/node100.jks"+"\n"
writef.write(writeStr)


writeStr = "USERNAME=ayadavum"+"\n"
writef.write(writeStr)



writeStr = "GIGAPAXOS_DATA_DIR=/home/GNSDir"+"\n"
writef.write(writeStr)


#writeStr = "MAX_GROUP_SIZE=40"+"\n"
#writef.write(writeStr)



writef.close()



writef = open("gnsclient.emulab.properties", "w")


writeStr = "CLIENT_SSL_MODE=SERVER_AUTH"+"\n"
writef.write(writeStr)


curr = 0

while(curr < NumNodes):
    nodeId = curr
    nodeName = "serv"+str(nodeId)
        
    
    key="reconfigurator.RC"+str(NumNodes)+"."+str(nodeId)
    writeStr = key+"="+str(nodeName)+":2178"+"\n"
    
    writef.write(writeStr)
    
    
    curr = curr + 1


writef.close()