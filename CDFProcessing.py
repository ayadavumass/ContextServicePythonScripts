# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
#!/usr/bin/python
import os
from CDFProcessInternal import CDFProcess
from mystat import get_stats_with_names

dirName = '/home/adipc/Documents/ContextServiceExperiments/LoadExpGNS/queryTimeGuidRes'
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

meanWriteF = open("meanQueryTime.txt", "w")

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
    
    #if(queryOrUpdate == 'queryOutput'):
    currList = CDFProcess(dirName+'/'+x)
    
    writef = open("QueryTimeCDF-"+guidString+".txt", "w")
    
    for index in range(len(currList)):
        totalReqPerc = (1.0 * (index+1))/len(currList)
        writeStr = str(currList[index])+','+str(totalReqPerc)+"\n"
        writef.write(writeStr)
        
    writef.close()
    
    res=get_stats_with_names(currList)
    writeStr=str(guidString)+','+str(res['mean'])+','+str(res['perc5'])+','+str(res['perc95'])+"\n"
    meanWriteF.write(writeStr)

meanWriteF.close()