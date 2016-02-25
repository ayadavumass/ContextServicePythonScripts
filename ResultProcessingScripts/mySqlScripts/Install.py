#!/usr/bin/python
import os, sys

lines = [line.strip() for line in open("nodeList.txt")]

# installing
for index in range(len(lines)):
    print "Installing mysql on "+lines[index]
    
    cmd = '/home/ayadav/mysqlScripts/install.sh mysqlDir-'+lines[index]
    os.system(cmd)