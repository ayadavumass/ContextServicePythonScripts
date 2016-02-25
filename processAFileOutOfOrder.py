#!/usr/bin/python

from mystat import get_stats_with_names

def processFile(filePath, searchStr1, searchStr2):
    lines = [line.strip() for line in open(filePath)]
    
    RequestStartDict    = {}
    RequestEndDict      = {}
    
    
    #TimeOutTime         = 1000000
    
    for index in range(len(lines)):
        line = lines[index]
        
        if ( line.find(searchStr1) != -1 ):
            parsed              = line.split(' ')
            lineQPStartTime     = long(parsed[7])
            lineRequestID       = int(parsed[5])
           
            RequestStartDict[lineRequestID] = lineQPStartTime
            
        if ( line.find(searchStr2) != -1 ):
            parsed = line.split(' ')
            lineQPEndTime = long(parsed[9])
 
            lineRequestID = int(parsed[5])
            RequestEndDict[lineRequestID] = lineQPEndTime
    
    AvgList = []
    
    for key in RequestStartDict:
        #reqTime = TimeOutTime
        if (RequestEndDict.has_key(key)):
            reqTime = RequestEndDict.get(key) - RequestStartDict.get(key)
            AvgList.append(reqTime)
        
    statDict = get_stats_with_names(AvgList)
    return statDict