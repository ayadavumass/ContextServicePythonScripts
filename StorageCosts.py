#!/bin/python
import math
M = 100
B = 30
N = 100
K = 3
V = 4
epsilon = 1
H = 3
A = 3
lamda = 100
rho = 200

ReplicateAll    = float( M * B * N * K * V )
QueryAll        = float( M * B * K * V )
#ValuePart      = M * B * K * (V + 1)
contextnet      = float( M * B * K * (V + 1) + B * epsilon )
Hyperdex        = float( M * B * V * (B/H + 1) )
Mercury         = float( M * B * V * B )
#Arpeggio        = M * B * V * pow(B,A)
#EfficientP2PS   = M * B * V
SIENNA          = float( M * B * N * V )


print "ReplicateAll " + str(ReplicateAll)
print "QueryAll " + str(QueryAll) 
#print "ValuePart " + str(ValuePart)
print "contextnet " + str(contextnet)
print "Hyperdex " + str(Hyperdex)
print "Mercury " + str(Mercury)
#print "Arpeggio " + str(Arpeggio)
#print "EfficientP2PS " + str(EfficientP2PS)
print "SIENNA " + str(SIENNA)


total = float(ReplicateAll+QueryAll+contextnet+Hyperdex+Mercury+SIENNA)

writef = open("StorageCost.csv", "w")
writeStr = "ReplicateAll, "+ str(ReplicateAll/total) +"\n"
writef.write(writeStr)

writeStr = "QueryAll, "+ str(QueryAll/total) +"\n"
writef.write(writeStr)

writeStr = "contextnet, "+ str(contextnet/total) +"\n"
writef.write(writeStr)

writeStr = "Hyperdex, "+ str(Hyperdex/total) +"\n"
writef.write(writeStr)

writeStr = "Mercury, "+ str(Mercury/total) +"\n"
writef.write(writeStr)

writeStr = "SIENNA, "+ str(SIENNA/total) +"\n"
writef.write(writeStr)

writef.close()