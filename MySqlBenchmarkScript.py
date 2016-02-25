#!/usr/bin/python
import os, time

numGuids                 = [10000]
searchRate               = [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 4000, 6000, 8000, 10000]
#queryIntervals          = [10, 20, 30, 40, 50]

for sr in searchRate:
    for ng in numGuids:
        print "executing " + str(sr)
        
        cmd = '/home/ayadav/mysqlScripts/CreateDB.py '
        os.system(cmd)
        
        time.sleep(5)
        
        cmd = '/home/ayadav/contextServiceScripts/mysqlTest/runMySqlBenchmarkOnNode.sh '+str(ng) +' '+str(sr)
        os.system(cmd)