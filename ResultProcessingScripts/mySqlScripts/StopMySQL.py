#!/usr/bin/python
import os, sys

lines = [line.strip() for line in open("nodeList.txt")]

# stoping
for index in range(len(lines)):
    print "Stoping mysql on "+lines[index]
    
    cmd = '/home/ayadav/mysqlScripts/stopMySQL.sh '+lines[index]+' mysqlDir-'+lines[index]
    os.system(cmd)