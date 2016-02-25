#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#hyperdex add-space -h 127.0.0.1 -p 1982 << EOF
#     space phonebook
#     key username
#     attributes first, last, int phone
#     tolerate 0 failures
#EOF

import os, sys, time

numAttrs = sys.argv[1]

fileName = "contextspace"+numAttrs+".sh"
#lines = [line.strip() for line in open("contextServiceList.txt")]
#initialPort = 5000

writef = open(fileName, "w")

writeStr = "#!/bin/bash"+"\n"
writef.write(writeStr)

writeStr = "hyperdex add-space -h serv0 -p 4999 << EOF"+"\n"
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

#initialPort = initialPort + 1
writef.close()

time.sleep(2)

os.system('chmod +x '+fileName)