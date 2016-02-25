#!/usr/bin/python
import os
from processFileOutOrderQuery import processFile
from mystat import get_stats_with_names


dirName = '/Users/ayadav/Documents/GNS/ContextServiceExpScripts/loadResults/queryResults5NodesLinear'
fileList = os.listdir(dirName)
print fileList

writef = open("QPT.csv", "w")
value_dict = {}
loadIndex  = {}
loadIndex['10-2'] = 10
loadIndex['20-4'] = 20
loadIndex['30-6'] = 30
loadIndex['40-8'] = 40
loadIndex['50-10'] = 50

for x in fileList:
    if ( x == '.svn'):
        continue
    
    fI = x.find('-',0)
    sI = x.find('-',fI+1)
    tI = x.find('-',sI+1)
    fTI = x.find('-',tI+1)
    ffI = x.find('-',fTI+1)
    sxI = x.find('-',ffI+1)
    svI = x.find('-',sxI+1)
    
    schemeTypeString = x[sI+1:tI ]
    uIntervalString = x[fTI+1:ffI]
    qIntervalString = x[sxI+1:svI]
    
    key = loadIndex[uIntervalString+'-'+qIntervalString]
    
    print x+' '+schemeTypeString+' '+schemeTypeString
    
    currList = processFile(dirName+'/'+x, 'QUERYFROMUSER REQUEST', 'QUERYFROMUSERREPLY REQUEST')
    
    if (not value_dict.has_key(key) ):
        exptTypeDict = {}
        meanList = []
        meanList.append(currList['mean'])
        exptTypeDict[schemeTypeString] = meanList
        value_dict[key] = exptTypeDict
    else:
        exptTypeDict = value_dict[key]
        
        if (not exptTypeDict.has_key(schemeTypeString) ):
            meanList = []
            meanList.append(currList['mean'])
            exptTypeDict[schemeTypeString] = meanList
        else:
            exptTypeDict[schemeTypeString].append(currList['mean'])
    
#if ( not statDict.has_key('ZEROVALUES') ):
#print value_dict

Keys=sorted(value_dict.keys())

for ui in Keys:
    exptTypeDict = value_dict[ui]
    writeStr=str(ui)
    for st in exptTypeDict:
        res=get_stats_with_names(exptTypeDict[st])
        writeStr+=','+str(st)+','+str(res['mean'])+','+str(res['perc5'])+','+str(res['perc95'])
    writeStr+="\n"
    writef.write(writeStr)
    
writef.close()