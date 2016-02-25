#!/bin/bash
javac -cp gns-cli-1.13-2014-12-17.jar ClearStoredKeys.java
java -cp gns-cli-1.13-2014-12-17.jar:. ClearStoredKeys
