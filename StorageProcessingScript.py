#!/usr/bin/python
from ProcessACSDirectoryStorage import processCSDirectory

result_dict = {}

lines = [line.strip() for line in open("100nodesSetup.txt")]

for index in range(len(lines)):
    node = lines[index].split( )
    print node[1]
    print "processing localDir on "+lines[index]
    
    #cmd = '/home/ayadav/runContextService.sh '+node[1]+' '+str(node[0])
    #cmd = 'mkdir /home/ayadav/localDir-'+node[1]+'-'+str(node[0])
    #os.system(cmd)
    
    #cmd = 'cp -rf 100nodesSetup.txt /home/ayadav/localDir-'+node[1]+'-'+str(node[0])
    #os.system(cmd)
    nodeID = str(node[0])
    dirName = '/home/ayadav/StorageResults/localDir-'+node[1]+'-'+str(node[0])
    
    result_dict[nodeID] = processCSDirectory(dirName)
    
    
final_dict = {}

for ni in result_dict.keys():
    node_dict = result_dict[ni]
    for expkey in node_dict.keys():
        if (final_dict.has_key(expkey)):
            final_dict[expkey]+=node_dict[expkey]
        else:
            final_dict[expkey]=node_dict[expkey]
    
write_dict = {}
for expKey in final_dict.keys():
    parsed = expKey.split('-')
    schemeS = int(parsed[0])
    attrS = int(parsed[1])
    
    if(write_dict.has_key(attrS)):
        write_dict[attrS][schemeS] = final_dict[expKey]
    else:
        scheme_dict = {}
        scheme_dict[schemeS] = final_dict[expKey]
        write_dict[attrS] = scheme_dict
    

writef = open("StoragevsB.csv", "w")
attrKeys = sorted(write_dict.keys())
for attrK in attrKeys:
    schemeKeys = sorted(write_dict[attrK].keys())
    writeStr=str(attrK)
    for sKeys in schemeKeys:
        writeStr+=','+str(sKeys)+','+str(write_dict[attrK][sKeys])
    writeStr+="\n"
    writef.write(writeStr)
    
writef.close()