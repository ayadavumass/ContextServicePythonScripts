#!/bin/bash
# set in admin mode
wget http://10.255.255.231:8080/GNS/admin?passkey=10.255.255.231:8080
# set it to high value
wget http://10.255.255.231:8080/GNS/setParameter?name=maxguids\&value=10000000
# get maxGuids
wget http://10.255.255.231:8080/GNS/getParameter?name=maxguids
