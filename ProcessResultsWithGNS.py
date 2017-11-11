#!/usr/bin/python
import os
from QueryTimeProcessingGNS import queryProcess
from UpdateTimeProcessingGNS import updateProcess
from mystat import get_stats_with_names


dirName = '/home/adipc/Documents/ContextServiceExperiments/LoadExpGNS/TimevsLoadResultsv2'
fileList = os.listdir(dirName)
print fileList

#value_dict         = {}
#loadIndex          = {}
#loadIndex['10-2']  = 10
#loadIndex['20-4']  = 20
#loadIndex['30-6']  = 30
#loadIndex['40-8']  = 40
#loadIndex['50-10'] = 50

updateMap = {}
queryMap  = {}

for x in fileList:
    if ( x == '.svn'):
        continue
    if ( x.startswith('writerOutput')):
        continue
    
    fI = x.find('-',0)
    sI = x.find('-',fI+1)
    tI = x.find('-',sI+1)
    fTI = x.find('-',tI+1)
    ffI = x.find('-',fTI+1)
    sxI = x.find('-',ffI+1)
    svI = x.find('-',sxI+1)
    etI = x.find('-', svI+1)
    ntI = x.find('-', etI+1)
    tnI = x.find('-', ntI+1)
    elI = x.find('-', tnI+1)
    twI = x.find('-', elI+1)
    
    #queryOrUpdate = x[0:fI]
    schemeTypeString = x[sI+1:tI]
    reqpsString = x[fTI+1:ffI]
    ratioString = x[sxI+1:svI]
    guidString = x[twI+1:]
    
    key = reqpsString+'-'+ratioString+'-'+guidString
    print x+' '+schemeTypeString+' '+reqpsString+' '+ratioString+' '+guidString
    
    #if(queryOrUpdate == 'queryOutput'):
    currList = queryProcess(dirName+'/'+x)
    if ( currList.has_key('ZEROVALUES') ):
        currList['mean'] = 0
        print "\n\n zero found \n\n"

    if (not queryMap.has_key(key) ):
        exptTypeDict = {}
        meanList = []
        meanList.append(currList['mean'])
        exptTypeDict[schemeTypeString] = meanList
        queryMap[key] = exptTypeDict
    else:
        exptTypeDict = queryMap[key]

        if (not exptTypeDict.has_key(schemeTypeString) ):
            meanList = []
            meanList.append(currList['mean'])
            exptTypeDict[schemeTypeString] = meanList
        else:
            exptTypeDict[schemeTypeString].append(currList['mean'])
        
    #elif (queryOrUpdate == 'updateOutput'):
    currList = updateProcess(dirName+'/'+x)
    
    if ( currList.has_key('ZEROVALUES') ):
        currList['mean'] = 0
        print "\n\n zero found \n\n"

    if (not updateMap.has_key(key) ):
        exptTypeDict = {}
        meanList = []
        meanList.append(currList['mean'])
        exptTypeDict[schemeTypeString] = meanList
        updateMap[key] = exptTypeDict
    else:
        exptTypeDict = updateMap[key]

        if (not exptTypeDict.has_key(schemeTypeString) ):
            meanList = []
            meanList.append(currList['mean'])
            exptTypeDict[schemeTypeString] = meanList
        else:
            exptTypeDict[schemeTypeString].append(currList['mean'])

#if ( not statDict.has_key('ZEROVALUES') ):
#print value_dict

writef = open("QPT.csv", "w")

Keys=sorted(queryMap.keys())

for ui in Keys:
    exptTypeDict = queryMap[ui]
    writeStr=str(ui)
    for st in exptTypeDict:
        res=get_stats_with_names(exptTypeDict[st])
        writeStr+=','+str(st)+','+str(res['mean'])
    writeStr+="\n"
    writef.write(writeStr)
    
writef.close()

writef = open("UPT.csv", "w")

Keys=sorted(updateMap.keys())

for ui in Keys:
    exptTypeDict = updateMap[ui]
    writeStr=str(ui)
    for st in exptTypeDict:
        res=get_stats_with_names(exptTypeDict[st])
        writeStr+=','+str(st)+','+str(res['mean'])
    writeStr+="\n"
    writef.write(writeStr)
    
writef.close()