#!/usr/bin/python
import os
from mystat import get_stats_with_names


dirName = '/home/GNSDir/queryTimeResults'
fileList = os.listdir(dirName)
print fileList


updateMap  = {}
searchMap  = {}
triggerMap  = {}

def processFile(numNodes, reqesPs, filePath):
    lines = [line.strip() for line in open(filePath)]
    
    searchResult                = []
    updateResult                = []
    triggerResult               = []
    
    for index in range(len(lines)):
        line = lines[index]

        if ( (line.find('Search reply recvd') != -1) and (line.find('TimeOut') == -1) ):        
            parsed               = line.split(' ')
            queryTime            = int(parsed[7])      
            searchResult.append(queryTime)
            
        if ( (line.find('LocUpd reply recvd') != -1) and (line.find('TimeOut') == -1) ):
            parsed               = line.split(' ')
            updateTime           = int(parsed[6])
            updateResult.append(updateTime)
        
        if ( (line.find('Trigger recvd time') != -1) and (line.find('TimeOut') == -1) ):
            parsed               = line.split(' ')
            triggerTime          = int(parsed[4])
            triggerResult.append(triggerTime)
            
    #result.sort()
    #result = result[(len(result)*10//100)+1:len(result)*90//100]
    statDict = get_stats_with_names(searchResult)
    if( searchMap.has_key(numNodes) ):
        requestDict = searchMap[numNodes]
        requestDict[reqesPs] = statDict['mean']
        searchMap[numNodes] = requestDict
    else:
        requestDict = {}
        requestDict[reqesPs] = statDict['mean']
        searchMap[numNodes] = requestDict
    
    statDict = get_stats_with_names(updateResult)
    if( updateMap.has_key(numNodes) ):
        requestDict = updateMap[numNodes]
        requestDict[reqesPs] = statDict['mean']
        updateMap[numNodes] = requestDict
    else:
        requestDict = {}
        requestDict[reqesPs] = statDict['mean']
        updateMap[numNodes] = requestDict
        
    
    statDict = get_stats_with_names(triggerResult)
    if( triggerMap.has_key(numNodes) ):
        requestDict = triggerMap[numNodes]
        requestDict[reqesPs] = statDict['mean']
        triggerMap[numNodes] = requestDict
    else:
        requestDict = {}
        requestDict[reqesPs] = statDict['mean']
        triggerMap[numNodes] = requestDict
    return


for x in fileList:
    if ( x == '.svn'):
        continue
    
    parsed     = x.split('-')
    
    numNodesString = parsed[6]
    reqpsString = parsed[10]
    
    processFile( int(numNodesString), int(reqpsString), dirName+'/'+x )




Keys=sorted(searchMap.keys())

for nnKeys in Keys:
    writef = open("searchTime"+str(nnKeys)+"nodes"+".csv", "w")
    reqestDict = searchMap[nnKeys]
    reqKeys=sorted(reqestDict.keys())
    
    for st in reqKeys:
        writeStr=str(st)+","+str(reqestDict[st])+"\n"
        writef.write(writeStr)
    
    writef.close()
    
Keys=sorted(updateMap.keys())
for nnKeys in Keys:
    writef = open("updateTime"+str(nnKeys)+"nodes"+".csv", "w")
    reqestDict = updateMap[nnKeys]
    reqKeys=sorted(reqestDict.keys())
    
    for st in reqKeys:
        writeStr=str(st)+","+str(reqestDict[st])+"\n"
        writef.write(writeStr)
    
    writef.close()


Keys=sorted(triggerMap.keys())
for nnKeys in Keys:
    writef = open("triggerTime"+str(nnKeys)+"nodes"+".csv", "w")
    reqestDict = triggerMap[nnKeys]
    reqKeys=sorted(reqestDict.keys())
    
    for st in reqKeys:
        writeStr=str(st)+","+str(reqestDict[st])+"\n"
        writef.write(writeStr)
    
    writef.close()