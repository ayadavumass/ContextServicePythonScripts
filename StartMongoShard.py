# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#!/usr/bin/python
import os, time

mainDir = '/home/ayadav/mongoShardScripts/'

cmd = mainDir+'KillMongo.py'
os.system(cmd)

cmd = 'rm -rf '+mainDir+'configdb-1'
os.system(cmd)

#cmd = 'rm -rf '+mainDir+'configdb-2'
#os.system(cmd)

#cmd = 'rm -rf '+mainDir+'configdb-3'
#os.system(cmd)

cmd = 'mkdir '+mainDir+'configdb-1'
os.system(cmd)

#cmd = 'mkdir '+mainDir+'configdb-2'
#os.system(cmd)

#cmd = 'mkdir '+mainDir+'configdb-3'
#os.system(cmd)

cmd = mainDir+'runMongoDConfig.sh compute-0-23 1'
os.system(cmd)

#cmd = mainDir+'runMongoDConfig.sh compute-0-14 2'
#os.system(cmd)

#cmd = mainDir+'runMongoDConfig.sh compute-0-15 3'
#os.system(cmd)

time.sleep(10)

# starting mongos on each 10 compute nodes
cmd = mainDir+'RunMongoS.py'
os.system(cmd)


# start mongd instances at different ports.

# remove directories, create directories
cmd = mainDir+'RemoveMongoDir.py'
os.system(cmd)

# make dirs
cmd = mainDir+'CreateDirMongo.py'
os.system(cmd)

# run mongod process
cmd = mainDir+'RunMongoD.py'
os.system(cmd)

time.sleep(10)

#adding all shards
cmd = 'mongo --host compute-0-13 --port 27017 '+mainDir+'mongoShell.js'
os.system(cmd)

# enable sharding on database and collections
cmd = 'mongo --host compute-0-13 --port 27017 '+mainDir+'enableShard.js'
os.system(cmd)