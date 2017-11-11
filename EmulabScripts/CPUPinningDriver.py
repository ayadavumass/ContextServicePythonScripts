
#!/bin/python
import os

CPUS_PER_VM     = 4
TOTAL_CPUS      = 32

Dom0Name        = 'Domain-0'

lastMachineName = ''
cpuNum          = 0
nodeMap         = {}
DIRNAME         ='/proj/MobilityFirst/ayadavDir/contextServiceScripts'


def writeTheCPUPinScript(vmlist):
    writef = open(DIRNAME+"/"+"cpuPinOnNode.sh", "w")
    cpunum = 0
    
    for vmname in vmlist:
        curr = 0
        while(curr < CPUS_PER_VM):
            cmd = 'sudo xl vcpu-pin '+vmname+' '+str(curr)+' '+str(cpunum)
            writef.write(cmd+"\n")
            print cmd+"\n"
            curr = curr + 1
            cpunum = cpunum + 1
    
    lastCpuNum = TOTAL_CPUS - 1
    cmd = 'sudo xl vcpu-pin '+Dom0Name+' all '+str(cpunum)+'-'+str(lastCpuNum)
    writef.write(cmd+"\n")
    print cmd+"\n"
    writef.close()
    

with open('nodeLayout.txt') as readf:
    for line in readf:
        
        line = line.rstrip()
        lines = line.split()
        
        vmName = lines[0]
        expName = lines[1]        
        
        currMachineName = vmName.split('-')[0]
        
        if(nodeMap.has_key(currMachineName)):
            vmlist = nodeMap[currMachineName]
            vmlist.append(vmName)
            nodeMap[currMachineName] = vmlist
        
        else:
            vmlist = []
            vmlist.append(vmName)
            nodeMap[currMachineName] = vmlist
            
readf.close()
    

for key in nodeMap:
    vmlist = nodeMap[key]
    
    # create the file
    writeTheCPUPinScript(vmlist)
    
    # make it executable
    cmd = 'chmod +x '+DIRNAME+"/"+"cpuPinOnNode.sh"
    os.system(cmd)
    
    
    
    # execute it
    cmd = 'bash '+DIRNAME+"/"+"cpuPin.sh"
    os.system(cmd)
    

