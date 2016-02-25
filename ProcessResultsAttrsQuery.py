#!/usr/bin/python
import os
from processFileOutOrderQuery import processFile
from mystat import get_stats_with_names

dirName = '/Users/ayadav/Documents/GNS/ContextServiceExpScripts/attrsResults/queryResultsvsAttrsLowLoad2'
fileList = os.listdir(dirName)
print fileList

writef = open("QPTvsAttrs.csv", "w")
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
    
    fI = x.find('scheme',0)
    sI = x.find('attrNum',0)
    
    schemeTypeString = x[fI+7:fI+8 ]
    attrNumString = x[sI+8:]
    
    print x+' '+schemeTypeString+' '+attrNumString
    
    currList = processFile(dirName+'/'+x, 'QUERYFROMUSER REQUEST', 'QUERYFROMUSERREPLY REQUEST')
    
    if (not value_dict.has_key(int(attrNumString)) ):
        schemeTypeDict = {}
        meanList = []
        meanList.append(currList['mean'])
        schemeTypeDict[int(schemeTypeString)] = meanList
        value_dict[int(attrNumString)] = schemeTypeDict
    else:
        exptTypeDict = value_dict[int(attrNumString)]
        
        if (not exptTypeDict.has_key(int(schemeTypeString)) ):
            meanList = []
            meanList.append(currList['mean'])
            exptTypeDict[int(schemeTypeString)] = meanList
        else:
            exptTypeDict[int(schemeTypeString)].append(currList['mean'])
    
#if ( not statDict.has_key('ZEROVALUES') ):
Keys=sorted(value_dict.keys())

for attr in Keys:
    exptTypeDict = value_dict[attr]
    writeStr=str(attr)
    
    stKeys=sorted(exptTypeDict.keys())
    for st in stKeys:
        res=get_stats_with_names(exptTypeDict[st])
        writeStr+=','+str(st)+','+str(res['mean'])+','+str(res['perc5'])+','+str(res['perc95'])
    writeStr+="\n"
    writef.write(writeStr)
    
writef.close()