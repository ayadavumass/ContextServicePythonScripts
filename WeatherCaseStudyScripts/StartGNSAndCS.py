#!/usr/bin/python
import os, sys

mainDir="/proj/MobilityFirst/ayadavDir"

cmd = mainDir+'/contextServiceScripts/startCSInstaller.sh' 
os.system(cmd)

cmd = mainDir+'/contextServiceScripts/startGNSInstaller.sh' 
os.system(cmd)