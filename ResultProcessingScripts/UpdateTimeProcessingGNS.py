#!/usr/bin/python

from mystat import get_stats_with_names

def updateProcess(filePath):
    
    lines = [line.strip() for line in open(filePath)]

    result               = []
    #numAttr              = int('-1')
    updateTime            = int('-1')

    #QPT_dict             = {}
    #QPResult_dict        = {}
    #Q_dict              = {}
    #QResult_dict        = {}

    for index in range(len(lines)):
        line = lines[index]

        if ( (line.find('Update reply recvd') != -1) and 
        (line.find('TimeOut') == -1) ):
            parsed              = line.split(' ')
            updateTime           = int(parsed[7])
            
            result.append(updateTime)
            
    #result.sort()
    #result = result[(len(result)*10//100)+1:len(result)*90//100]
    statDict = get_stats_with_names(result)
    return statDict