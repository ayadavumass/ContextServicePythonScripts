#!/usr/bin/python
import os, time

cmd = '/home/ayadav/KillJava.py'
os.system(cmd)
print "COntext service killed"        
#cmd = '/home/ayadav/killAll.sh compute-0-23'
#os.system(cmd)
        
cmd = '/home/ayadav/killAll.sh compute-0-24'
os.system(cmd)
print "update query shut"

os.system('/usr/bin/java -cp /home/ayadav/gns-cli-1.14-2015-1-16.jar:/home/ayadav ClearStoredKeys')
print "Stored keys deleted"

os.system('rm -rf /home/ayadav/localDir-compute-0-*')
print "local dir gone"

os.system('/home/ayadav/restartGNS.sh compute-0-23')
print "GNS restarted"
time.sleep(10)

os.system('/usr/bin/java -jar /home/ayadav/gns-cli-1.14-2015-1-16.jar < /home/ayadav/setupGNSAccount.gns')
print "GNS account created"

os.system('/home/ayadav/gnsGUIDIncreaseScript.sh')
print "Increased max guids"

os.system('/home/ayadav/CreateDir.py')