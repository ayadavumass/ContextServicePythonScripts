#! /usr/bin/python

#!/bin/python

lines = [line.strip() for line in 
    open("/home/adipc/Documents/ContextServiceExperiments/QueryTimevsAttributes/guidOut_SingleNode1ps")]


valList              = []
QPT_dict             = {}
QPResult_dict        = {}
#Q_dict              = {}
#QResult_dict        = {}

for index in range(len(lines)):
    line = lines[index]
    parsed          = line.split(' ')
    time = int(parsed[3])
    valList.append(time)

valList.sort()
i = 1.0
writef = open("/home/adipc/Documents/ContextServiceExperiments/QueryTimevsAttributes/PRguidOut_SingleNode1ps", "w")
for timeval in valList:
    perc = ((float)(i * 1.0))/len(lines)
    writeStr = str(perc)+','+str(timeval)+"\n"
    writef.write(writeStr)
    i=i+1.0;

writef.close()