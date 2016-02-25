#!/usr/bin/python
import os

result_dict = {}

dirName = '/proj/MobilityFirst/ayadavDir/updateThroughputResults/updateResultsServ22'
fileList = os.listdir(dirName)
#print fileList


for x in fileList:
    if ( x == '.svn'):
        continue
    
    if ( x.find('requestOutput-users') == -1 ):
        continue
    
    parsed = x.split('-')
    
    numUsers = parsed[2]
    numNodes = parsed[12]
    
    fileObj = open(dirName+'/'+x)
    
    eventualRate = -1
    goodput = -1
    
    for line in fileObj:
            
        if(line.find("LocationUpd result:Goodput") != -1):
            #print line
            parsed = line.split(' ')
            try:
                goodput = float(parsed[2])
            except ValueError:
                print("Oops!  wrong line")
                continue
        
        if( line.find("LocationUpd eventual sending rate") != -1 ):
            #print line
            parsed = line.split(' ')
            try:
                eventualRate = float(parsed[4])
            except ValueError:
                print("Oops!  wrong line")
                continue
    fileObj.close()
    
    if( result_dict.has_key(numNodes) ):
            numUserDict = result_dict[numNodes]
            if(numUserDict.has_key(numUsers)):
                numUserDict[numUsers] = numUserDict[numUsers] + goodput
            else:
                numUserDict[numUsers] = goodput
    else:
        numUserDict = {}
        numUserDict[numUsers] = goodput
        result_dict[numNodes] = numUserDict
        

dirName = '/proj/MobilityFirst/ayadavDir/updateThroughputResults/updateThroughputResultsServ23'
fileList = os.listdir(dirName)
#print fileList


for x in fileList:
    if ( x == '.svn'):
        continue
    
    if ( x.find('requestOutput-users') == -1 ):
        continue
    
    parsed = x.split('-')
    
    numUsers = parsed[2]
    numNodes = parsed[12]
    
    fileObj = open(dirName+'/'+x)
    
    eventualRate = -1
    goodput = -1
    
    for line in fileObj:
            
        if(line.find("LocationUpd result:Goodput") != -1):
            #print line
            parsed = line.split(' ')
            try:
                goodput = float(parsed[2])
            except ValueError:
                print("Oops!  wrong line")
                continue
        
        if( line.find("LocationUpd eventual sending rate") != -1 ):
            #print line
            parsed = line.split(' ')
            try:
                eventualRate = float(parsed[4])
            except ValueError:
                print("Oops!  wrong line")
                continue
    fileObj.close()
    
    if( result_dict.has_key(numNodes) ):
            numUserDict = result_dict[numNodes]
            if(numUserDict.has_key(numUsers)):
                numUserDict[numUsers] = numUserDict[numUsers] + goodput
            else:
                numUserDict[numUsers] = goodput
    else:
        numUserDict = {}
        numUserDict[numUsers] = goodput
        result_dict[numNodes] = numUserDict
        

graphDict = {}
for numNodesKey in result_dict:
    numUserDict = result_dict[numNodesKey]
    gmax = -1
    for userKey in numUserDict:
        goodput = numUserDict[userKey]
    
        if(goodput > gmax):
            gmax = goodput
    graphDict[numNodesKey] = gmax
    
writef = open("updateThroughputVsNumNodes", "w")
sortedKeys = sorted(graphDict.iterkeys(), key=int)
for numNodesKey in sortedKeys:
    goodput = graphDict[numNodesKey]
    writeStr = str(numNodesKey)+","+str(goodput)+"\n"
    writef.write(writeStr)

writef.close()