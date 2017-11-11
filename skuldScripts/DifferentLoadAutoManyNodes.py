#!/usr/bin/python
import os, time

#schemes
CONTEXTNET               = 1
REPLICATE_ALL            = 2
QUERY_ALL                = 3
MERCURY                  = 4

# update intervals
#schemeTypes             = [CONTEXTNET, REPLICATE_ALL, QUERY_ALL, MERCURY]
schemeTypes              = [CONTEXTNET, REPLICATE_ALL, QUERY_ALL]
#schemeTypes             = [MERCURY]
#updateIntervals         = [2000, 4000, 6000, 8000, 10000]
updateRate               = [50, 40, 30, 20, 10]
#queryIntervals          = [10, 20, 30, 40, 50]

# 300 seconds
expDurUsed               = 300 # 5 min

for ur in updateRate:
    for scheme in schemeTypes:
        print "Executing scheme "+ str(scheme)
        print "executing " + str(ur)
        cmd = '/home/ayadav/RunContextService.py '+str(scheme)
        os.system(cmd)
        # sleep for 2 mins for system to start
        time.sleep(100)
        
        # start update load
        cmd = '/home/ayadav/StartUpdateLoad.py '+str(scheme)+' '+str(ur)+' '+str(ur/5)
        os.system(cmd)
        
        # wait for 10 seconds
        # time.sleep(10)
        
        # start update load
        cmd = '/home/ayadav/StartQueryLoad.py '+str(scheme)+' '+str(ur)+' '+str(ur/5)
        os.system(cmd)
        
        # wait for 60 seconds, for results to finish
        time.sleep(expDurUsed)
        
        cmd = '/home/ayadav/killAll.sh compute-0-23'
        os.system(cmd)
        
        cmd = '/home/ayadav/killAll.sh compute-0-24'
        os.system(cmd)
        
        cmd = '/home/ayadav/KillJava.py'
        os.system(cmd)