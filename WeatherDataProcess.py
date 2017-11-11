#!/bin/python
import os
from mystat import get_stats_with_names


lines = [line.strip() for line in open("/home/adipc/Documents/ContextServiceExperiments/WeatherCaseStudyExps/SingleNodeResults/GNSServiceOutput")]

contextTime         = []
gnsTime             = []

for index in range(len(lines)):
    line = lines[index]
    
    if ( line.find('ContextService search results results') != -1 ):
        parsed              = line.split(' ')
        timeTaken           = int(parsed[6])
        contextTime.append(timeTaken)
        
    if ( line.find('GNS search results results') != -1 ):
        parsed = line.split(' ')
        timeTaken = int(parsed[6])
        gnsTime.append(timeTaken)
        
        
if(len(contextTime) > 0):
    statDict = get_stats_with_names(contextTime)
    print "context time mean "+str(statDict['mean'])+','+str(statDict['perc5'])+','+str(statDict['perc95'])

if(len(gnsTime) > 0):
    statDict = get_stats_with_names(gnsTime)
    print "gns time mean "+str(statDict['mean'])+','+str(statDict['perc5'])+','+str(statDict['perc95'])