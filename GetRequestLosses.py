# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


#!/usr/bin/python
import os

def processGetRequestLosses(dirName):
    
    fileList = os.listdir(dirName)
    print fileList

    querySentMap  = {}
    queryComplMap = {}

    updateSentMap = {}
    updateComplMap = {}
    
    for x in fileList:
        if ( x == '.svn'):
            continue
        
        if ( x.find('requestOutput-scheme') == -1 ):
            continue
        
        parts = x.split('-')
        
        ratio = parts[6]
        reqsps = parts[4]
        scheme = parts[2]
        
        key = scheme+'-'+reqsps+'-'+ratio
        
        querySent  = 0
        queryRepliesRecvd = 0
        
        updateSent = 0
        updateRepliesRecvd = 0
    
        fileObj = open(dirName+'/'+x)
        for line in fileObj:
            
            if(line.find("JointRequestsWithMissPoisson:QUERY") != -1):
                querySent = querySent + 1
            elif ( (line.find('MSOCKETWRITERINTERNAL from CS') != -1) and (line.find('TimeOut') == -1) ):
                queryRepliesRecvd = queryRepliesRecvd + 1
            elif(line.find("JointRequestsWithMissPoisson:UPDATE") != -1):
                updateSent = updateSent + 1
            elif ( (line.find('Update reply recvd') != -1) and (line.find('TimeOut') == -1) ):
                updateRepliesRecvd = updateRepliesRecvd + 1    
        fileObj.close()
        
        
        if (not querySentMap.has_key(key) ):
            querySentMap[key] = querySent
        else:
            querySentMap[key] = querySentMap[key]+querySent
        
        if (not queryComplMap.has_key(key) ):
            queryComplMap[key] = queryRepliesRecvd
        else:
            queryComplMap[key] = queryComplMap[key]+queryRepliesRecvd
        
        
        if (not updateSentMap.has_key(key) ):
            updateSentMap[key] = updateSent
        else:
            updateSentMap[key] = updateSentMap[key]+updateSent
        
        if (not updateComplMap.has_key(key) ):
            updateComplMap[key] = updateRepliesRecvd
        else:
            updateComplMap[key] = updateComplMap[key]+updateRepliesRecvd
    
    #print "queryRecvdMap "+queryRecvdMap+" queryComplMap "+queryComplMap
    
    Keys=sorted(querySentMap.keys())

    for ks in Keys:
        qa = querySentMap[ks] * 1.0
        rs = queryComplMap[ks] * 1.0
        print "\n querySentMap[ks] "+str(querySentMap[ks]) +" queryComplMap[ks] "+str(queryComplMap[ks])
        loss = 0.0
        loss = ((qa - rs) * 100.0)/qa
        print "key "+str(ks)+"loss "+str(loss)
    
    print "\n\n"
    for ks in Keys:
        qa = updateSentMap[ks] * 1.0
        rs = updateComplMap[ks] * 1.0
        print "\n updateSentMap[ks] "+str(updateSentMap[ks]) +" updateComplMap[ks] "+str(updateComplMap[ks])
        loss = 0.0
        loss = ((qa - rs) * 100.0)/qa
        print "key "+str(ks)+"loss "+str(loss)
    
    
processGetRequestLosses('/home/adipc/Documents/ContextServiceExperiments/LoadExpGNS/resultHypCons')