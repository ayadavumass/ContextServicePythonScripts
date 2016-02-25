# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from mystat import get_stats_with_names

import os

dirName = '/home/ayadav/contextServiceScripts/requestOutput/test'
fileList = os.listdir(dirName)
print fileList

#value_dict         = {}
#loadIndex          = {}
#loadIndex['10-2']  = 10
#loadIndex['20-4']  = 20
#loadIndex['30-6']  = 30
#loadIndex['40-8']  = 40
#loadIndex['50-10'] = 50
valueUpdateMega = {}
refreshMega = {}

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
    
    filePath = dirName+'/'+x
    
    lines = [line.strip() for line in open(filePath)]
    
    valueUpdateMap   = {}
    refreshMap       = {}
    
    for index in range(len(lines)):
        line = lines[index]

        if ( line.find('Sending update requestID') != -1 ):
            
            parsed              = line.split(' ')
            reqNum              = long(parsed[3])
            stime                = long(parsed[5])
            valueUpdateMap[reqNum] = stime
            valueUpdateMega[reqpsString] = valueUpdateMap
        
        elif (line.find('RefreshTrigger completion requestID') != -1):
            parsed              = line.split(' ')
            reqNum              = long(parsed[3])
            stime                = long(parsed[5])
            refreshMap[reqNum] = stime
            refreshMega[reqpsString] = refreshMap


Keys=sorted(refreshMega.keys())

meanWriteF = open("meanRefreshTime.txt", "w")

for ki in Keys:
    currRefreshMap = refreshMega[ki]
    currValueUpdateMap = valueUpdateMega[ki]
    
    #indKs=sorted(currRefreshMap.keys())
    indKs=sorted(currValueUpdateMap.keys())
    timeList = []
    
    for inki in indKs:
        if(currRefreshMap.has_key(inki)):
            timeList.append(currRefreshMap[inki] - currValueUpdateMap[inki])
        else:
            print "No Refresh caused "+str(inki)
            
        
    timeList.sort()
    
    res=get_stats_with_names(timeList)
    writeStr=str(ki)+','+str(res['mean'])+','+str(res['perc5'])+','+str(res['perc95'])+"\n"
    meanWriteF.write(writeStr)

meanWriteF.close()