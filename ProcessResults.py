#!/bin/python
import os
from mystat import get_stats_with_names

#myList = []
#f = open("workingPlanetlab40.txt","r") #opens file with name of "test.txt"
#myList = f.readlines()

lines = [line.strip() for line in open("dataFiles/contextOutputMercuryU3")]

#print(lines)
#for line in f:
#    myList.append(str(line))

#f.close()
#currNumAttr     = -1
#currRequestID   = -1
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
                #if(reqTime > 0 and reqTime < 1000):
                QPNumAttrList.append(QPTime)
                QP_dict[currNumAttr] = QPNumAttrList
                
                
                QNumAttrList = []
                QTime = (int)(QEndTime - QStartTime)
                #if(reqTime > 0 and reqTime < 1000):
                QNumAttrList.append(QTime)
                Q_dict[currNumAttr] = QNumAttrList
                
            else:
                QPNumAttrList = QP_dict[currNumAttr]
                QPTime = (int)(QPEndTime - QPStartTime)
                #if(reqTime > 0 and reqTime < 1000):
                QPNumAttrList.append(QPTime)
                
                QNumAttrList = Q_dict[currNumAttr]
                QTime = (int)(QEndTime - QStartTime)
                #if(reqTime > 0 and reqTime < 1000):
                QNumAttrList.append(QTime)
            
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
        
        if ( (lineRequestID == currRequestID) and (lineNumAttr == currNumAttr) ):
            QPEndTime = lineQPEndTime
            QEndTime = lineQEndTime
    
print QP_dict
print Q_dict

for key in QP_dict:
    valList = QP_dict[key]
    valList.sort()
    valList = valList[(len(valList)*10//100)+1:len(valList)*90//100]
    statDict = get_stats_with_names(valList)
    if ( not statDict.has_key('ZEROVALUES') ):
        QPResult_dict[key] = str(statDict['mean'])+','+str(statDict['perc5'])+','+str(statDict['perc95'])
        
print QPResult_dict

writef = open("resultDir/contextOutputMercuryU3QP.csv", "w")
sortedKeys = sorted(QPResult_dict.iterkeys(), key=int)
for key in sortedKeys:
    writeStr = str(key)+','+QPResult_dict[key]+"\n"
    writef.write(writeStr)

writef.close()


for key in Q_dict:
    valList = Q_dict[key]
    valList.sort()
    valList = valList[(len(valList)*10//100)+1:len(valList)*90//100]
    statDict = get_stats_with_names(valList)
    if ( not statDict.has_key('ZEROVALUES') ):
        QResult_dict[key] = str(statDict['mean'])+','+str(statDict['perc5'])+','+str(statDict['perc95'])
        
print QResult_dict

writef = open("resultDir/contextOutputMercuryU3Q.csv", "w")
sortedKeys = sorted(QResult_dict.iterkeys(), key=int)
for key in sortedKeys:
    writeStr = str(key)+','+QResult_dict[key]+"\n"
    writef.write(writeStr)

writef.close()

    #print "Killing java on "+lines[index]
    
    #cmd = '/Users/ayadav/Documents/GNS/ContextServiceExpScripts/killAll.sh '+lines[index]
    #os.system(cmd)