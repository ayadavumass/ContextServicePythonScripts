#!/usr/bin/python
import os, time

CSScriptOutputDir = "/proj/MobilityFirst/ayadavDir/ContextNetGitHub/contextnet/conf/emulabConf/contextServiceConf"
homeDir = "/home"
GNSScriptOutputDir = "/proj/MobilityFirst/ayadavDir/GNSGithub/GNS/conf/emulabConf"

mainDir  = "/proj/MobilityFirst/ayadavDir"

numNodes = [8]


for numnodes in numNodes:
    cmd = mainDir+'/contextServiceScripts/VaryingNodesScript.py '+str(numnodes)+' '+CSScriptOutputDir+' '+homeDir+' '+GNSScriptOutputDir
    os.system(cmd)
    time.sleep(2)
  
    cmd = mainDir+'/contextServiceScripts/ResetAll.py'
    os.system(cmd)
    time.sleep(10)


    cmd = mainDir+'/mysqlScripts/Start.py'
    os.system(cmd)
    
    time.sleep(10)
    cmd = mainDir+'/mysqlScripts/CreateDB.py'
    os.system(cmd)
            
    
    cmd = mainDir+'/contextServiceScripts/StartGNSAndCS.py'
    os.system(cmd)
    time.sleep(10)
        
    # start weather and mobility load
    #cmd = mainDir+'/contextServiceScripts/StartRequestLoad.py '+str(scheme)+' '+str(reqsps)+' '+str(ratio)+' '+str(numAttr)+' '+str(guids) +' '+str(numnodes)
    #os.system(cmd)
    #print "request load started"

# kill the last one.
#cmd = mainDir+'/contextServiceScripts/KillProcesses.py'
#os.system(cmd)
#print "Java and killed"

#cmd = mainDir+'/mongoShardScripts/KillMongo.py'
#os.system(cmd)