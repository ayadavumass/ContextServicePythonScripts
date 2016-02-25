#!/bin/python
import os
from mystat import get_stats_with_names

#myList = []
#f = open("workingPlanetlab40.txt","r") #opens file with name of "test.txt"
#myList = f.readlines()

lines = [line.strip() for line in open("dataFiles/contextOutputContextNetU3")]

#print(lines)
#for line in f:
#    myList.append(str(line))

#f.close()
#currNumAttr        = -1
#currRequestID      = -1
currNumAttr         = int('-1')
QStartTime          = int('-1')
QEndTime            = int('-1')
QPStartTime         = long('-1')
QPEndTime           = long('-1')
currRequestID       = int('-1')
QP_dict             = {}
QPResult_dict       = {}
Q_dict              = {}
QResult_dict        = {}

TimeOutTime         = 3000

for index in range(len(lines)):
    line = lines[index]
    
    if ( line.find('CONTEXTSERVICE EXPERIMENT: QUERYFROMUSER REQUEST ID') != -1 ):
        parsed              = line.split(' ')
        lineCurrNumAttr     = int(parsed[7])
        lineQPStartTime     = long(parsed[9])
        lineRequestID       = int(parsed[5])
        lineQStartTime      = int(parsed[12])
        
        # new request write previous one
        if( (lineRequestID != currRequestID) and (currRequestID != -1) ):
            if (not QP_dict.has_key(currNumAttr) ):
                QPNumAttrList = []
                QPTime = (int)(QPEndTime - QPStartTime)
                
                if(QPTime > 0):
                    QPNumAttrList.append(QPTime)
                else:
                    QPNumAttrList.append(TimeOutTime)
                
                QP_dict[currNumAttr] = QPNumAttrList
                
                
                QNumAttrList = []
                QTime = (int)(QEndTime - QStartTime)
                
                if(QTime > 0):
                    QNumAttrList.append(QTime)
                else:
                    QNumAttrList.append(TimeOutTime)
                
                Q_dict[currNumAttr] = QNumAttrList
                
            else:
                QPNumAttrList = QP_dict[currNumAttr]
                QPTime = (int)(QPEndTime - QPStartTime)
                
                if(QPTime > 0):
                    QPNumAttrList.append(QPTime)
                else:
                    QPNumAttrList.append(TimeOutTime)
                    
                    
                QNumAttrList = Q_dict[currNumAttr]
                QTime = (int)(QEndTime - QStartTime)
                #if(reqTime > 0 and reqTime < 1000):
                if(QTime > 0):
                    QNumAttrList.append(QTime)
                else:
                    QNumAttrList.append(TimeOutTime)
            
            currNumAttr     = lineCurrNumAttr
            QPStartTime     = lineQPStartTime
            currRequestID   = lineRequestID
            QPEndTime       = long('-1')
            QStartTime      = lineQStartTime
            QEndTime        = long('-1')
            
        elif ( currRequestID == -1 ):
            currNumAttr = lineCurrNumAttr
            QPStartTime = lineQPStartTime
            QStartTime  = lineQStartTime
            currRequestID = lineRequestID
        
        
    if ( line.find('CONTEXTSERVICE EXPERIMENT: QUERYFROMUSERREPLY REQUEST ID') != -1 ):
        parsed = line.split(' ')
        lineNumAttr = int(parsed[7])
        lineQPEndTime = long(parsed[9])
        lineQEndTime = long(parsed[11])
        lineRequestID = int(parsed[5])
        
        if ( (lineRequestID == currRequestID) ):
            QPEndTime = lineQPEndTime
            QEndTime = lineQEndTime
    
print QP_dict
print Q_dict

Mean = []

for key in QP_dict:
    valList = QP_dict[key]
    valList.sort()
    #valList = valList[(len(valList)*10//100)+1:len(valList)*90//100]
    statDict = get_stats_with_names(valList)
    if ( not statDict.has_key('ZEROVALUES') ):
        Mean.append(statDict['mean'])
        #QPResult_dict[key] = str(statDict['mean'])+','+str(statDict['perc5'])+','+str(statDict['perc95'])
        
print Mean
statDict = get_stats_with_names(Mean)
writef = open("resultDir/contextOutputContextNetU3QP.csv", "w")
#sortedKeys = sorted(QPResult_dict.iterkeys(), key=int)
#for key in sortedKeys:
writeStr = str(statDict['mean'])+','+str(statDict['perc5'])+','+str(statDict['perc95'])+"\n"
writef.write(writeStr)

writef.close()