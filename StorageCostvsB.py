#!/bin/python
import math
M = 100
B = 10
N = 100
K = 3
V = 4
epsilon = 1
H = 3
A = 3
lamda = 100
rho = 200

writef = open("StorageCostvsB.csv", "w")

for x in xrange(1, 11):
    ReplicateAll    = float( M * B * N * K * V )
    QueryAll        = float( M * B * K * V )

    contextnet      = float( M * B * K * (V + 1) + B * epsilon )
    Hyperdex        = float( M * B * V * (B/H + 1) )
    Mercury         = float( M * B * V * B )

    SIENNA          = float( M * B * N * V )
    
    #total = float(ReplicateAll+QueryAll+contextnet+Hyperdex+Mercury+SIENNA)
    total = 1
    writeStr = str(B)+","+ str(contextnet/total) +","+ str(ReplicateAll/total) +","+str(QueryAll/total)+","+str(Mercury/total)+","+str(Hyperdex/total)+","+str(SIENNA/total)+"\n"
    writef.write(writeStr)
    B = B + 10

writef.close()