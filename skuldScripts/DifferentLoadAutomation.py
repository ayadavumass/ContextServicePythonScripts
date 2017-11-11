#!/usr/bin/python
import os, time

mainDir = "/home/ayadav"

#schemes
CONTEXTNET           = 1
REPLICATE_ALL        = 2
QUERY_ALL            = 3
MERCURY              = 4
HYPERDEX	         = 5
MERCURYNEW	         = 6
MERCURYCONSISTENT    = 7

# update intervals
schemeTypes          = [MERCURYCONSISTENT]
#schemeTypes         = [REPLICATE_ALL, CONTEXTNET, QUERY_ALL]
#schemeTypes         = [CONTEXTNET]
#updateIntervals     = [2000, 4000, 6000, 8000, 10000]
requestPerSec	     = [400]
#requestPerSec       = [10, 50, 90, 130, 170, 210, 250, 290]
#updateIntervals     = [2000]

#queryIntervals      = [10, 20, 30, 40, 50]
numAttr		         = 100
#ratioList           = [0.1, 0.25, 0.50, 0.75, 0.9]
#ratioList           = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
ratioList	         = [0.5]
#numGUIDs	         = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
numGUIDs	         = [1000]

# 300 seconds
expDuration          = 999999
expDurUsed           = 100 # 5 min

for guids in numGUIDs:
  for reqsps in requestPerSec:
     for ratio in ratioList:
        for scheme in schemeTypes:
            print "Executing scheme "+ str(scheme)
            print "executing " + str(reqsps)
	    
            cmd = mainDir+'/contextServiceScripts/ResetAll.py'
            os.system(cmd)
            time.sleep(10)

            # start hyperdex if scheme is hyperdex
            if( (scheme == HYPERDEX) or (scheme == MERCURYNEW) ):
		cmd = 'rm -rf '+mainDir+'/hyperdexData/dataDir-compute*'
		os.system(cmd)
		cmd = 'rm -rf '+mainDir+'/hyperdexData/coordDir'
                os.system(cmd)

		cmd = mainDir+'/hyperdexScripts/CreateDataDir.py'
                os.system(cmd)
		
		time.sleep(5)
		
		cmd = mainDir+'/hyperdexScripts/StartHyperdex.py'
		os.system(cmd)
            
            if( scheme == MERCURYCONSISTENT ):
                cmd = mainDir+'/mongoShardScripts/StartMongoShard.py'
		os.system(cmd)
                
                time.sleep(10)
            
        
            cmd = mainDir+'/contextServiceScripts/RunContextService.py '+str(scheme)+' '+str(numAttr)+' '+str(reqsps)+' '+str(ratio)
            os.system(cmd)
            # sleep for 2 mins for system to start
            time.sleep(150)
	    
            # start update load
            cmd = mainDir+'/contextServiceScripts/StartRequestLoad.py '+str(scheme)+' '+str(reqsps)+' '+str(ratio)+' '+str(numAttr)+' '+str(guids)
            os.system(cmd)
            print "request load started"
            # wait for 10 seconds
            # time.sleep(10)
        
            # start update load
            #cmd = '/home/ayadav/StartQueryLoad.py '+str(scheme)+' '+str(ui)+' '+str(ui/100)
            #os.system(cmd)
            #print "query load started"
            # wait for 300 seconds for results to finish
            #time.sleep(expDurUsed)

# kill the last one.
cmd = mainDir+'/contextServiceScripts/KillProcesses.py'
os.system(cmd)
print "Java and hyperdex killed"


cmd = mainDir+'/mongoShardScripts/KillMongo.py'
os.system(cmd)