#!/usr/bin/python
import os

def processCSDirectory(dirName):
    
    fileList = os.listdir(dirName)
    print fileList

    queryRecvdMap = {}
    queryComplMap = {}
    
    for x in fileList:
        if ( x == '.svn'):
            continue
        
        if ( x.find('contextOutputcompute') == -1 ):
            continue
        
        parts = x.split('-')
        
        ratio = parts[11]
        reqsps = parts[9]
        scheme = parts[7]
        
        key = scheme+'-'+reqsps+'-'+ratio
        
        queryRecvd  = 0
        repliesSent = 0
    
        fileObj = open(dirName+'/'+x)
        for line in fileObj:
            
            if(line.find("QUERY RECVD") != -1):
                queryRecvd = queryRecvd + 1
            elif(line.find("QUERY COMPLETE") != -1):
                repliesSent = repliesSent + 1
                
        fileObj.close()
        
        
        if (not queryRecvdMap.has_key(key) ):
            queryRecvdMap[key] = queryRecvd
        else:
            queryRecvdMap[key] = queryRecvdMap[key]+queryRecvd
        
        if (not queryComplMap.has_key(key) ):
            queryComplMap[key] = repliesSent
        else:
            queryComplMap[key] = queryComplMap[key]+repliesSent
    
    #print "queryRecvdMap "+queryRecvdMap+" queryComplMap "+queryComplMap
    
    Keys=sorted(queryRecvdMap.keys())

    for ks in Keys:
        qa = queryRecvdMap[ks] * 1.0
        rs = queryComplMap[ks] * 1.0
        print "queryRecvdMap[ks] "+str(queryRecvdMap[ks]) +" queryComplMap[ks] "+str(queryComplMap[ks])
        loss = 0.0
        loss = ((qa - rs) * 100.0)/qa
        print "key "+str(ks)+"loss "+str(loss)
        
    
    
processCSDirectory('/home/adipc/Documents/ContextServiceExperiments/LoadExpGNS/contextServiceOutput')