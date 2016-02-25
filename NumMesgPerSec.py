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

ReplicateAll    = M * B * lamda * (N-1) + rho
QueryAll        = M * B * lamda * K + N * rho
contextnet      = 4 * M * B * lamda * K + 2 * B * rho
Hyperdex        = 2 * M * B * lamda * (B/H + 1) + rho
Mercury         = 2 * M * B * lamda * B + rho
SIENNA          = M * B * lamda * (N-1) + N * rho

writef = open("NumMesgPerSec.csv", "w")

for x in xrange(1, 11):
    lamda           = 100 * x
    rho             = 200 * x
    ReplicateAll    = float(M * B * lamda * (N-1) + rho)
    QueryAll        = float(M * B * lamda * K + N * rho)
    contextnet      = float(4 * M * B * lamda * K + 2 * B * rho)
    Hyperdex        = float(2 * M * B * lamda * (B/H + 1) + rho)
    Mercury         = float(2 * M * B * lamda * B + rho)
    SIENNA          = float(M * B * lamda * (N-1) + N * rho)
    
    totalMesg = float(ReplicateAll+QueryAll+contextnet+Hyperdex+Mercury+SIENNA)
    
    
    writeStr = str(x)+","+ str(ReplicateAll/totalMesg) +","+ str(QueryAll/totalMesg) +","+str(contextnet/totalMesg)+","+str(Hyperdex/totalMesg)+","+str(Mercury/totalMesg)+","+str(SIENNA/totalMesg)+"\n"
    writef.write(writeStr)

writef.close()