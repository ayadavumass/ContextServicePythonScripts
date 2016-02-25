#! /usr/bin/python

import os, sys, time

numAttrs = sys.argv[1]
#lines = [line.strip() for line in open("contextServiceList.txt")]
#initialPort = 5000
fileName = "contextspace"+numAttrs+".sh"
writef = open(fileName, "w")

writeStr = "#!/bin/bash"+"\n"
writef.write(writeStr)

# main searchable keyspace.

writeStr = "hyperdex add-space -h compute-0-23 -p 4999 << EOF"+"\n"
writef.write(writeStr)

writeStr = "space contextnet"+"\n"
writef.write(writeStr)

writeStr = "key GUID"+"\n"
writef.write(writeStr)

writeStr = "attributes "

#     space phonebook
#     key username
#     attributes first, last, int phone
#     subspace first, last, phone
#     tolerate 0 failures
#EOF

for x in range(0, int(numAttrs)):
    name = "float contextATT"+str(x)
    writeStr = writeStr + name
    if ( not ( x == (int(numAttrs)-1) ) ):
        writeStr = writeStr + ", "
    
writeStr = writeStr + "\n"
writef.write(writeStr)

writeStr = "tolerate 0 failures"+"\n"
writef.write(writeStr)

writeStr = "EOF"+"\n"
writef.write(writeStr)

writeStr = "echo \" contexnet Comp\""+"\n"
writef.write(writeStr)

# creating range keyspaces.

for x in range(0, int(numAttrs)):
    #time.sleep(3)
    writeStr = "sleep 1"+"\n"
    writef.write(writeStr)
    
    writeStr = "echo \" starting "+ str(x)+"\""+"\n"
    writef.write(writeStr)
    
    
    writeStr = "hyperdex add-space -h compute-0-23 -p 4999 << EOF"+"\n"
    writef.write(writeStr)

    writeStr = "space contextATT"+str(x)+"Keyspace"+"\n"
    writef.write(writeStr)

    writeStr = "key rangeKey"+"\n"
    writef.write(writeStr)

    writeStr = "attributes float lowerRange, float upperRange"+"\n"
    writef.write(writeStr)
    
    writeStr = "tolerate 0 failures"+"\n"
    writef.write(writeStr)

    writeStr = "EOF"+"\n"
    writef.write(writeStr)


writeStr = "echo \" rangekeyspace \""+"\n"
writef.write(writeStr)
    
#rangeKey keyspace
writeStr = "hyperdex add-space -h compute-0-23 -p 4999 << EOF"+"\n"
writef.write(writeStr)

writeStr = "space rangeKeyspace"+"\n"
writef.write(writeStr)

writeStr = "key rangeKey"+"\n"
writef.write(writeStr)

writeStr = "attributes map activeQueryMap"+"\n"
writef.write(writeStr)

writeStr = "tolerate 0 failures"+"\n"
writef.write(writeStr)

writeStr = "EOF"+"\n"
writef.write(writeStr)

writef.close()

os.system('chmod +x '+fileName)