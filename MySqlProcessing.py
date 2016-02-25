# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from mystat import get_stats_with_names

import os

dirName = '/home/adipc/Documents/ContextServiceExperiments/LoadExpGNS/timeoutresultsv2'
fileList = os.listdir(dirName)
print fileList

#value_dict         = {}
#loadIndex          = {}
#loadIndex['10-2']  = 10
#loadIndex['20-4']  = 20
#loadIndex['30-6']  = 30
#loadIndex['40-8']  = 40
#loadIndex['50-10'] = 50
timeMapReqsps       = {}



for x in fileList:
    if ( x == '.svn'):
        continue
    
    fI = x.find('-',0)
    sI = x.find('-',fI+1)
    #tI = x.find('-',sI+1)
    
    #queryOrUpdate = x[0:fI]
    #schemeTypeString = x[sI+1:tI]
    reqpsString = x[sI+1:]
    #ratioString = x[sxI+1:svI]
    #guidString = x[twI+1:]
    #clientID = x[etI+1:ntI]
    
    
    #key = reqpsString+'-'+ratioString+'-'+guidString
    key = int(reqpsString)
    print x+' '+reqpsString
    
    filePath = dirName+'/'+x
    
    lines = [line.strip() for line in open(filePath)]
    
    sendMap             = {}
    compMap             = {}
    
    for index in range(len(lines)):
        line = lines[index]
        
        if ( line.find('Time taken') != -1 ):
            #print line
            parsed              = line.split(' ')
            stime               = long(parsed[2])
            #sendMap[reqNum] = stime
            
            if ( timeMapReqsps.has_key(key) ):
                currList = timeMapReqsps[key]
                currList.append(stime)
                timeMapReqsps[key] = currList
            else:
                currList = []
                currList.append(stime)
                timeMapReqsps[key] = currList

Keys=sorted(timeMapReqsps.keys())

meanWriteF = open("meanQueryTime.txt", "w")

for ki in Keys:
    currList = timeMapReqsps[ki]
    #currList.sort()
    
    res=get_stats_with_names(currList)
    writeStr=str(ki)+','+str(res['mean'])+','+str(res['perc5'])+','+str(res['perc95'])+"\n"
    meanWriteF.write(writeStr)

meanWriteF.close()