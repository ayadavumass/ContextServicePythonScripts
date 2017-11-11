#!/usr/bin/python
import os
from mystat import get_stats_with_names

bulkGetMap          = {}
processValueNodeMap = {}

def processCSDirectory(dirName):
    global bulkGetMap
    global processValueNodeMap
    
    fileList = os.listdir(dirName)
    print fileList
    
    for x in fileList:
        if ( x == '.svn'):
            continue
        
        if ( x.find('contextOutputcompute') != -1 ):
            parts = x.split('-')
        
            ratio = parts[11]
            reqsps = parts[9]
            scheme = parts[7]
        
            #key = scheme+'-'+reqsps+'-'+ratio
            key = int(reqsps)
            
            fileObj = open(dirName+'/'+x)
            print x
            for line in fileObj:
                try:
                    if(line.find("DelayMeasure: processBulkGet") != -1):

                        lp = line.split(' ')
                        nt = int(lp[2])
                        if (not bulkGetMap.has_key(key) ):
                            tlist = []
                            tlist.append(nt)
                            bulkGetMap[key] = tlist
                        else:
                            tlist = bulkGetMap[key]
                            tlist.append(nt)
                            bulkGetMap[key] = tlist

                    elif(line.find("DelayMeasure: processQueryMsgToValuenode") != -1):
                        lp = line.split(' ')
                        nt = int(lp[2])
                        if (not processValueNodeMap.has_key(key) ):
                            tlist = []
                            tlist.append(nt)
                            processValueNodeMap[key] = tlist
                        else:
                            tlist = processValueNodeMap[key]
                            tlist.append(nt)
                            processValueNodeMap[key] = tlist
                except ValueError:
                    print "Oops!  That was no valid number.  Try again..."
                    
            fileObj.close()
    
            #print "queryRecvdMap "+queryRecvdMap+" queryComplMap "+queryComplMa

fileList = os.listdir('/home/ayadav/contextServiceScripts/')
print fileList


for x in fileList:
    if ( x == '.svn'):
        continue
        
    if ( x.find('localDir-compute-') != -1 ):
        print x
        processCSDirectory('/home/ayadav/contextServiceScripts/'+x)

#prints
writef = open("bulkGet.csv", "w")
bkKeys = bulkGetMap.keys()
bkKeys.sort()
for key in bkKeys:
    valList = bulkGetMap[key]
    #valList.sort()
    #valList = valList[(len(valList)*10//100)+1:len(valList)*90//100]
    statDict = get_stats_with_names(valList)
    if ( not statDict.has_key('ZEROVALUES') ):
        writeStr = str(key)+','+str(statDict['mean'])+','+str(statDict['perc5'])+','+str(statDict['perc95'])+"\n"
        writef.write(writeStr)
writef.close()


writef = open("processValue.csv", "w")

pvKeys = processValueNodeMap.keys()
pvKeys.sort()

for key in pvKeys:
    valList = processValueNodeMap[key]
    #valList.sort()
    #valList = valList[(len(valList)*10//100)+1:len(valList)*90//100]
    statDict = get_stats_with_names(valList)
    if ( not statDict.has_key('ZEROVALUES') ):
        writeStr = str(key)+','+str(statDict['mean'])+','+str(statDict['perc5'])+','+str(statDict['perc95'])+"\n"
        writef.write(writeStr)
writef.close()