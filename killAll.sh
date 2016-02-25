#!/bin/bash
ssh -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/id_rsa -l umass_nameservice $1 'killall -9 java'
#ssh -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/id_rsa -l umass_nameservice $1 '/home/umass_nameservice/setJavaPath.sh'
