#!/bin/python
M = 5
numAttr = [20, 40, 60, 80, 100]
B = 0
N = 100
K = 1
V = 4
epsilon = 1
H = 3
A = 3
lamda = float(1)
rho = 2

##contextnet      = 4 * M * B * lamda * K + 2 * B * rho
#ReplicateAll    = M * B * lamda * (N-1) + rho
#QueryAll        = M * B * lamda * K + N * rho
#Mercury         = 2 * M * B * lamda * B + rho
#Hyperdex        = 2 * M * B * lamda * (B/H + 1) + rho
#SIENNA          = M * B * lamda * (N-1) + N * rho

writef = open("ModelNumMesgvsB.csv", "w")

for x in numAttr:
    #lamda           = 100 * x
    #rho             = 200 * x
    B = x
    contextnet      = float(4 * M * B * lamda * K + 2 * B * rho)
    ReplicateAll    = float(M * B * lamda * (N-1) + rho)
    QueryAll        = float(M * B * lamda * K + N * rho)
    Mercury         = float(2 * M * B * lamda * B + rho)
    #Hyperdex        = float(2 * M * B * lamda * (B/H + 1) + rho)
    #SIENNA          = float(M * B * lamda * (N-1) + N * rho)
    
    #totalMesg = float(ReplicateAll+QueryAll+contextnet+Hyperdex+Mercury+SIENNA)
    total = 1
    
    writeStr = str(B)+",1,"+ str(contextnet/total) +",2,"+ str(ReplicateAll/total) +",3,"+str(QueryAll/total)+",4,"+str(Mercury/total)+"\n"
    writef.write(writeStr)

writef.close()