#!/bin/python
import os

CPUS_PER_VM     = 4
TOTAL_CPUS      = 32

Dom0Name        = 'Domain-0'

lastMachineName = ''
cpuNum          = 0
nodeMap         = {}

with open('nodeLayout.txt') as readf:
    for line in readf:
        
        line = line.rstrip()
        lines = line.split()
        
        vmName = lines[0]
        expName = lines[1]        
        
        currMachineName = vmName.split('-')[0]
        
        print "vmName "+vmName+" expName "+expName+" currMachineName "+currMachineName
        
        if( lastMachineName ==  currMachineName ):
            curr = 0
            while(curr < CPUS_PER_VM):
                cmd = 'sudo xl vcpu-pin '+vmName+' '+str(curr)+' '+str(cpuNum)
                print cmd+"\n"
                os.system(cmd)
                curr = curr + 1
                cpuNum = cpuNum + 1
            
            lastMachineName = currMachineName
        else:
            if(lastMachineName == ''):
                cpuNum = 0
                
                curr = 0
                while(curr < CPUS_PER_VM):
                    cmd = 'sudo xl vcpu-pin '+vmName+' '+str(curr)+' '+str(cpuNum)
                    print cmd+"\n"
                    os.system(cmd)
                    curr = curr + 1
                    cpuNum = cpuNum + 1
                
                lastMachineName = currMachineName
            else:
                # assign cpus to dom0
                lastCpuNum = TOTAL_CPUS - 1
                cmd = 'sudo xl vcpu-pin '+Dom0Name+' all '+str(cpuNum)+'-'+str(lastCpuNum)
                print cmd+"\n"
                os.system(cmd)
                
                cpuNum = 0
                
                curr = 0
                while(curr < CPUS_PER_VM):
                    cmd = 'sudo xl vcpu-pin '+vmName+' '+str(curr)+' '+str(cpuNum)
                    print cmd+"\n"
                    os.system(cmd)
                    curr = curr + 1
                    cpuNum = cpuNum + 1
                
                lastMachineName = currMachineName
                
                
            
            
        
        
readf.close()

