# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


#!/usr/bin/python

def CDFProcess(filePath):
    
    lines = [line.strip() for line in open(filePath)]

    result               = []
    #numAttr              = int('-1')
    queryTime            = int('-1')

    #QPT_dict             = {}
    #QPResult_dict        = {}
    #Q_dict              = {}
    #QResult_dict        = {}

    for index in range(len(lines)):
        line = lines[index]

        if ( (line.find('MSOCKETWRITERINTERNAL from CS') != -1) and 
        (line.find('TimeOut') == -1) ):
            
            parsed              = line.split(' ')
            queryTime           = int(parsed[4])
            numAttr             = long(parsed[6])
            
            result.append(queryTime)

    result.sort()
    return result