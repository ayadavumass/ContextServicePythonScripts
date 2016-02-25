#!/bin/bash
#scp -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/id_rsa ~/context-nodoc-0.1-2014-12-06.jar plabNodesInfo.txt runContextServiceOnNode.sh umass_nameservice@$1:/home/umass_nameservice/
#ssh -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/id_rsa -l umass_nameservice $1 '/home/umass_nameservice//runContextServiceOnNode.sh'
#ssh -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/id_rsa -l umass_nameservice $1 '/home/umass_nameservice/setJavaPath.sh'
#cat plabWorkingTested.txt | /usr/local/bin/parallel -j+100 scp -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/id_rsa ~/context-nodoc-0.1-2014-12-06.jar plabNodesInfo.txt runContextServiceOnNode.sh umass_nameservice@{}:
cat contextServiceList.txt | /usr/local/bin/parallel -j+100 ssh -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -l umass_nameservice {} '/home/umass_nameservice/runContextServiceOnNode.sh'

