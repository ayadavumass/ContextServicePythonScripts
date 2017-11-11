#!/bin/python

numAttrs = 40
attrPrefix='attr'
minVal = 1.0
maxVal = 1500.0
defaultVal = 1.0
dataType = 'Double'


writef = open("attributeInfo.txt", "w")

writeStr = "#attrName, minValue, maxValue, datatype[Integer, Long, Double, String]"+"\n"
writef.write(writeStr)

curr = 0
while(curr < numAttrs):
    writeStr \
    = attrPrefix+str(curr)+", "+str(minVal)+", "+str(maxVal)+", "+dataType+"\n"
    writef.write(writeStr)
        
    curr = curr + 1
    
writef.close()