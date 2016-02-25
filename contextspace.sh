#!/bin/bash
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextnet
key GUID
attributes float contextATT0, float contextATT1, float contextATT2, float contextATT3, float contextATT4, float contextATT5, float contextATT6, float contextATT7, float contextATT8, float contextATT9, float contextATT10, float contextATT11, float contextATT12, float contextATT13, float contextATT14, float contextATT15, float contextATT16, float contextATT17, float contextATT18, float contextATT19, float contextATT20, float contextATT21, float contextATT22, float contextATT23, float contextATT24, float contextATT25, float contextATT26, float contextATT27, float contextATT28, float contextATT29, float contextATT30, float contextATT31, float contextATT32, float contextATT33, float contextATT34, float contextATT35, float contextATT36, float contextATT37, float contextATT38, float contextATT39, float contextATT40, float contextATT41, float contextATT42, float contextATT43, float contextATT44, float contextATT45, float contextATT46, float contextATT47, float contextATT48, float contextATT49
tolerate 0 failures
EOF
echo " contexnet Comp"
sleep 1
echo " starting 0"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT0Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 1"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT1Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 2"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT2Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 3"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT3Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 4"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT4Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 5"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT5Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 6"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT6Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 7"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT7Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 8"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT8Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 9"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT9Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 10"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT10Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 11"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT11Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 12"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT12Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 13"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT13Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 14"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT14Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 15"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT15Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 16"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT16Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 17"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT17Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 18"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT18Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 19"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT19Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 20"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT20Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 21"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT21Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 22"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT22Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 23"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT23Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 24"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT24Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 25"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT25Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 26"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT26Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 27"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT27Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 28"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT28Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 29"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT29Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 30"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT30Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 31"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT31Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 32"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT32Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 33"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT33Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 34"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT34Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 35"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT35Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 36"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT36Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 37"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT37Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 38"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT38Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 39"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT39Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 40"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT40Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 41"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT41Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 42"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT42Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 43"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT43Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 44"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT44Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 45"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT45Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 46"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT46Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 47"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT47Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 48"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT48Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
sleep 1
echo " starting 49"
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space contextATT49Keyspace
key rangeKey
attributes float lowerRange, float upperRange
tolerate 0 failures
EOF
echo " rangekeyspace "
hyperdex add-space -h compute-0-23 -p 4999 << EOF
space rangeKeyspace
key rangeKey
attributes map activeQueryMap
tolerate 0 failures
EOF
