#! /usr/bin/python

#!/bin/python
from mystat import get_stats_with_names

#myList = []
#f = open("workingPlanetlab40.txt","r") #opens file with name of "test.txt"
#myList = f.readlines()

lines = [line.strip() for line in 
    open("/home/adipc/Documents/ContextServiceExperiments/QueryTimevsAttributes/result_CS30_v2")]

numAttr             = int('-1')
queryTime           = int('-1')

QPT_dict             = {}
QPResult_dict        = {}
#Q_dict              = {}
#QResult_dict        = {}

for index in range(len(lines)):
    line = lines[index]
    
    if ( line.find('MSOCKETWRITERINTERNAL from CS') != -1 ):
        parsed              = line.split(' ')
        queryTime           = int(parsed[4])
        numAttr             = long(parsed[6])
        
        if ( not QPT_dict.has_key(numAttr) ):
                QPTList = []
                #if(reqTime > 0 and reqTime < 1000):
                QPTList.append(queryTime)
                QPT_dict[numAttr] = QPTList
                
        else:
                QPTList = QPT_dict[numAttr]
                #if(reqTime > 0 and reqTime < 1000):
                QPTList.append(queryTime)


for key in QPT_dict:
    valList = QPT_dict[key]
    valList.sort()
    #valList = valList[(len(valList)*10//100)+1:len(valList)*90//100]
    statDict = get_stats_with_names(valList)
    if ( not statDict.has_key('ZEROVALUES') ):
        QPResult_dict[key] = str(statDict['mean'])+','+str(statDict['perc5'])+','+str(statDict['perc95'])
        
print QPResult_dict


writef = open("/home/adipc/Documents/ContextServiceExperiments/QueryTimevsAttributes/QPTAttrCS30v2", "w")
sortedKeys = sorted(QPResult_dict.iterkeys(), key=int)
for key in sortedKeys:
    writeStr = str(key)+','+QPResult_dict[key]+"\n"
    writef.write(writeStr)

writef.close()



# for GNS

lines = [line.strip() for line in 
    open("/home/adipc/Documents/ContextServiceExperiments/QueryTimevsAttributes/result_GNS_300")]

numAttr             = int('-1')
queryTime           = int('-1')

QPT_dict             = {}
QPResult_dict        = {}
#Q_dict              = {}
#QResult_dict        = {}

for index in range(len(lines)):
    line = lines[index]
    
    if ( line.find('MSOCKETWRITERINTERNAL from GNS') != -1 ):
        parsed              = line.split(' ')
        queryTime           = int(parsed[4])
        numAttr             = long(parsed[6])
        
        if ( not QPT_dict.has_key(numAttr) ):
                QPTList = []
                #if(reqTime > 0 and reqTime < 1000):
                QPTList.append(queryTime)
                QPT_dict[numAttr] = QPTList
                
        else:
                QPTList = QPT_dict[numAttr]
                #if(reqTime > 0 and reqTime < 1000):
                QPTList.append(queryTime)


for key in QPT_dict:
    valList = QPT_dict[key]
    valList.sort()
    #valList = valList[(len(valList)*10//100)+1:len(valList)*90//100]
    statDict = get_stats_with_names(valList)
    if ( not statDict.has_key('ZEROVALUES') ):
        QPResult_dict[key] = str(statDict['mean'])+','+str(statDict['perc5'])+','+str(statDict['perc95'])
        
print QPResult_dict

writef = open("/home/adipc/Documents/ContextServiceExperiments/QueryTimevsAttributes/QPTAttrGNS300", "w")
sortedKeys = sorted(QPResult_dict.iterkeys(), key=int)
for key in sortedKeys:
    writeStr = str(key)+','+QPResult_dict[key]+"\n"
    writef.write(writeStr)

writef.close()