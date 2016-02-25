#!/bin/bash
#ssh -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/planetlabKey -l umass_nameservice $1 'mkdir /home/umass_nameservice'
ssh -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/planetlabKey -l umass_nameservice $1 'mkdir ayadav'
#scp -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/planetlabKey ~/jdk1.7.0.tar.gz setJavaPath.sh  umass_nameservice@$1:/home/umass_nameservice/
scp -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/planetlabKey setJavaPath.sh  umass_nameservice@$1:/home/umass_nameservice/
ssh -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/planetlabKey -l umass_nameservice $1 'tar -zxvf jdk1.7.0.tar.gz'
ssh -q -oStrictHostKeyChecking=no -oConnectTimeout=5 -i ~/privatekey/planetlabKey -l umass_nameservice $1 '/home/umass_nameservice/setJavaPath.sh'
