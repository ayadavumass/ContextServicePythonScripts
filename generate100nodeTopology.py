#!/bin/python

lines = [line.strip() for line in open("contextServiceList.txt")]
initialPort = 5000

writef = open("100nodesSetup.txt", "w")

for x in range(0, 100):
    writeStr = str(x)+' '+lines[x%10]+' '+str(initialPort)+"\n"
    writef.write(writeStr)
    initialPort = initialPort + 1
    
writef.close()