#!/bin/bash
#ssh -q -oStrictHostKeyChecking=no -oConnectTimeout=5  -i ~/privatekey/id_rsa -l umass_nameservice $1 'hostname'
ssh -q -oStrictHostKeyChecking=no -oConnectTimeout=5  -i ~/privatekey/id_rsa -l umass_nameservice $1 'java -version'
