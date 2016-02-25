#!/usr/bin/python
import os, sys, time

lines = [line.strip() for line in open("nodeList.txt")]

# starting
port = 6000
for index in range(len(lines)):
    print "Starting mysql on "+lines[index]
    
    cmd = '/home/ayadav/mysqlScripts/startMySQL.sh mysqlDir-'+lines[index]+' '+str(port)+' '+lines[index]
    os.system(cmd)
    port = port + 1
    
    # 5 sec sleep
    time.sleep(5)
    cmd = '/home/ayadav/mysqlScripts/setRootPass.sh '+lines[index]
    os.system(cmd)