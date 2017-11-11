#!/usr/bin/python
import os

bconfigResult_dict = {}
rconfigResult_dict = {}


#print fileList
dirList = ['/proj/MobilityFirst/ayadavDir/throughputExpResults/searchThroughputResultsServ37', '/proj/MobilityFirst/ayadavDir/throughputExpResults/searchThroughputServ36' ]
for dirName in dirList:
    fileList = os.listdir(dirName)
    for x in fileList:
        if ( x == '.svn'):
            continue
    
        parsed     = x.split('-')
    
        searchRate = parsed[8]
        numNodes   = parsed[6]
        sconfig    = int(parsed[12])
    
        fileObj    = open(dirName+'/'+x)
    
        eventualRate = -1
        goodput = -1
    
        for line in fileObj:
            if(line.find("Search result:Goodput") != -1):
                #print line
                parsed = line.split(' ')
                try:
                    goodput = float(parsed[2])
                except ValueError:
                        print("Oops!  wrong line")
                        continue
        
            if( line.find("Search eventual sending rate") != -1 ):
                #print line
                parsed = line.split(' ')
                try:
                    eventualRate = float(parsed[4])
                except ValueError:
                    print("Oops!  wrong line")
                    continue
        fileObj.close()
    
        if(sconfig == 1):
            if( bconfigResult_dict.has_key(numNodes) ):
                srDict = bconfigResult_dict[numNodes]
                if(srDict.has_key(searchRate)):
                    srDict[searchRate] = srDict[searchRate] + goodput
                else:
                    srDict[searchRate] = goodput
            else:
                srDict = {}
                srDict[searchRate] = goodput
                bconfigResult_dict[numNodes] = srDict
        elif(sconfig == 2):
            if( rconfigResult_dict.has_key(numNodes) ):
                srDict = rconfigResult_dict[numNodes]
                if(srDict.has_key(searchRate)):
                    srDict[searchRate] = srDict[searchRate] + goodput
                else:
                    srDict[searchRate] = goodput
            else:
                srDict = {}
                srDict[searchRate] = goodput
                rconfigResult_dict[numNodes] = srDict
                
graphDict = {}
for numNodesKey in bconfigResult_dict:
    srDict = bconfigResult_dict[numNodesKey]
    gmax = -1
    for srKey in srDict:
        goodput = srDict[srKey]
    
        if(goodput > gmax):
            gmax = goodput
    graphDict[numNodesKey] = gmax
    
writef = open("searchThroughputVsNumNodesBaseConfig", "w")
sortedKeys = sorted(graphDict.iterkeys(), key=int)
for numNodesKey in sortedKeys:
    goodput = graphDict[numNodesKey]
    writeStr = str(numNodesKey)+","+str(goodput)+"\n"
    writef.write(writeStr)
    
writef.close()


graphDict = {}
for numNodesKey in rconfigResult_dict:
    srDict = rconfigResult_dict[numNodesKey]
    gmax = -1
    for srKey in srDict:
        goodput = srDict[srKey]
    
        if(goodput > gmax):
            gmax = goodput
    graphDict[numNodesKey] = gmax
    
writef = open("searchThroughputVsNumNodesRepConfig", "w")
sortedKeys = sorted(graphDict.iterkeys(), key=int)
for numNodesKey in sortedKeys:
    goodput = graphDict[numNodesKey]
    writeStr = str(numNodesKey)+","+str(goodput)+"\n"
    writef.write(writeStr)
    
writef.close()