#!/usr/bin/python

from mystat import get_stats_with_names

def processFile(filePath):
    lines = [line.strip() for line in open(filePath)]
    
    updateTimeList      = []
    readTimeList        = []
    
    updateStarted       = 0
    
    for index in range(len(lines)):
        line = lines[index]
        
        if ( line.find('attr Update Start') != -1 ):
            updateStarted       = 1
            parsed              = line.split(' ')
            updateStartTime     = int(parsed[3])
            
            
        if ( (line.find('Refresh trigger recvd') != -1) and ( updateStarted == 1 ) ):
            parsed = line.split(' ')
            updateEndTime = int(parsed[len(parsed)-1])
            updateTimeList.append(updateEndTime-updateStartTime)
            updateStarted = 0
        
        if ( line.find('getGroupMembersGUIDs time') != -1 ):
            parsed              = line.split(' ')
            readTime = int(parsed[len(parsed)-1])
            readTimeList.append(readTime)
        
    print "len "+str(len(updateTimeList))
    updateTimeList.sort()
    updateTimeList = updateTimeList[(len(updateTimeList)*10//100)+1:len(updateTimeList)*90//100]
    
    statDict = get_stats_with_names(updateTimeList)
    print "Mean update "+str(statDict['mean']) +" Min "+str(statDict['perc5']) +" max "+str(statDict['perc95'])
    
    print "len "+str(len(readTimeList))
    readTimeList.sort()
    readTimeList = readTimeList[(len(readTimeList)*10//100)+1:len(readTimeList)*90//100]
    
    statDictR = get_stats_with_names(readTimeList)
    print "Mean Read "+str(statDictR['mean']) +" Min "+str(statDictR['perc5']) +" max "+str(statDictR['perc95'])
    
    return statDict

processFile('contextResults18Marv3')