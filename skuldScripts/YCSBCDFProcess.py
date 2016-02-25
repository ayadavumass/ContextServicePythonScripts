# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


lines = [line.strip() for line in open("outWorkENumRec10KScan10K")]

numLinesToSkip = 7
currSkipLines  = 0
totalFinish = 0
timeArray = {}
numOper = 0

for index in range(len(lines)):
    line = lines[index]
    
    if ( line.find('SCAN') != -1 ):
        parsed              = line.split(',')
        currSkipLines = currSkipLines + 1
        if ( line.find('Operations') != -1 ):
            numOper = int(parsed[2])
            
        if ( (currSkipLines > numLinesToSkip) and (currSkipLines <= 10007) ):
            currTime            = int(parsed[1])
            timeIntFinish       = int(parsed[2])
            totalFinish = totalFinish + timeIntFinish
            
            timeArray[currTime] = totalFinish
            

writef = open("graphOutNumRec10KScan10K.txt", "w")

for key in timeArray:
    totalReqPerc = (1.0 * timeArray[key])/numOper
    writeStr = str(key)+','+str(totalReqPerc)+"\n"
    writef.write(writeStr)
            
writef.close()