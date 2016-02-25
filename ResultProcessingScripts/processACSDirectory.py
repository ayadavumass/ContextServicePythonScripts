#!/usr/bin/python
import os
from mystat import get_stats_with_names

def processCSDirectory(dirName):
    
    fileList = os.listdir(dirName)
    print fileList
    
    result_dict = {}

    for x in fileList:
        if ( x == '.svn'):
            continue
        
        if ( x.find('contextOutputcompute') == -1 ):
            continue
        
        fI = x.find('-',0)
        sI = x.find('-',fI+1)
        tI = x.find('-',sI+1)
        fTI = x.find('-',tI+1)
        ffI = x.find('-',fTI+1)
        sxI = x.find('-',ffI+1)
        svI = x.find('-',sxI+1)
        
        attrNumString = x[ffI+1:sxI]
        schemeTypeString = x[svI+1: ]
        numMesgList = []
        fileObj = open(dirName+'/'+x)
        for line in fileObj:
            
            if(line.find("NUM MESS") != -1):
                #print line
                parsed = line.split(' ')
                try:
                    lineNumMesg = int(parsed[6])
                    numMesgList.append(lineNumMesg)
                except ValueError:
                    print("Oops!  wrong line")
                    continue
        
        fileObj.close()
        
        # removing min value
        numMesgList = numMesgList[(len(numMesgList)*10//100)+1:len(numMesgList)*90//100]
        
        statDict = get_stats_with_names(numMesgList)
        
        key = schemeTypeString+'-'+attrNumString
        if (statDict.has_key('mean')):
            result_dict[key]=statDict['mean']
        else:
            print "bad exp: no mean key"
        
    return result_dict