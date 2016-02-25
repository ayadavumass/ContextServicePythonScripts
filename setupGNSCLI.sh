#!/bin/bash
scp -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/id_rsa ~/gns-cli-1.13-2014-12-17.jar ~/gnsumassAnanasKeys gnscli.sh ~/ClearStoredKeys.java clearStoredKeys.sh umass_nameservice@$1:/home/umass_nameservice/
ssh -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/id_rsa -l umass_nameservice $1 '/home/umass_nameservice/clearStoredKeys.sh'
ssh -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/id_rsa -l umass_nameservice $1 'java -jar gns-cli-1.13-2014-12-17.jar < gnscli.sh'
#ssh -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/id_rsa -l umass_nameservice $1 '/home/umass_nameservice/setJavaPath.sh'
