import math
from scipy.optimize import minimize
from scipy.optimize import fsolve

#result = minimize(f, [1])
#print(result.x)
rho        = 0.1
#Yc         = 1.0
N          = 36.0
# calculated by single node throughput, not very accurate estimation but let's go with that for now.
# specially if result size increases then estimation error might increase.
CsByC      = 1.0/(69.55366816958512 * 4.0)
CuByC      = 1.0/(153.74028685197356 * 4.0)
B          = 20.0
Aavg       = 4.0

#
# for calculating expected number of nodes a query goes to.
YByDArray = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

#def solveDAlpha(c):
#    x = sympy.Symbol('x')
#    res = sympy.solve(1.0 + x * (sympy.log(c) - sympy.log(x) + 1) - c, x)
#    
#    for i in range(len(res)):
#        if(res[i] > c):
#            return res[i]
#    return -1

def dAlphsFunc(x, c):
    if (x <= 0):
        return -1
    print "dAlphsFunc "+str(x) +" "+str(c)
    return 1.0 + x * (math.log(c) - math.log(x) + 1) - c

def solveDAlpha(c):
    data = (c)
    res = fsolve(dAlphsFunc, 1.0, args=data)
    print "solveDAlpha res.x "+str(res)
    for i in range(len(res)):
        if(res[i] > c):
            return res[i]
    # approximate it as c as paper says one root should be greater than c, i
    # if solver fails to find the root in 100 iterations
    return c

def calculateExpectedNumNodesASearchGoesTo(numNodesForSubspace, currH, currM):  
        numNodes = (float) (numNodesForSubspace*1.0)
        expectedNumNodes = 0.0
        # calculating expected value of the first term
        for ybdi in YByDArray:
            expectedNumNodes = expectedNumNodes + \
                ( math.ceil(ybdi * math.pow(numNodesForSubspace, (1.0/currH)) ) )
        prob = 1.0/(1.0*len(YByDArray))
        expectedNumNodes = expectedNumNodes * prob
        expectedNumNodes = math.pow(expectedNumNodes, currM)
        mByH = (currM * 1.0)/(currH * 1.0)
        
        # calculating expected value of the second term
        expectedNumNodes = expectedNumNodes * math.pow(numNodesForSubspace, 1-mByH)        
        return expectedNumNodes

def maxBallsFun(currH, Aavg, B):
    # optimizer sometimes sends negative values
    if(currH < 0):
        return 0.0

    m = Aavg
    n = math.ceil(B/currH)
    print "currH "+str(currH)+" m "+ str(m)+" n "+str(n)+" (n*math.log(n)) "+str((n*math.log(n)))
    alpha = 1.0
    if ( n== 1.0):
        return Aavg
    # all terms which can go negative are made zero
    # needed for the maths to hold
    if ( (m > 0) and (m < (n*math.log(n)) ) ):
        logNlogNByM = math.log( (n * math.log(n))/m )
        secondTerm = math.log(logNlogNByM)/logNlogNByM
        if(secondTerm < 0):
            secondTerm = 0
        retValue = (math.log(n)/logNlogNByM)*( 1+alpha * (secondTerm) )
        if(math.floor((n*math.log(n))/m) == 1.0):
            c = n*math.log(n)/m
            dAlpha = solveDAlpha(c)
            #dAlpha = 1.0
            retValue = (dAlpha -1 + alpha)*math.log(n)
        print "returned case 1 "+str(retValue)
        
        #return math.floor(retValue)
        return retValue
    elif ( (m >= n*math.log(n)) and m < n*math.pow(math.log(n),2) ):
        c = m/( n*math.log(n) )
        dAlpha = solveDAlpha(c)
        #dAlpha = 1.0
        retValue = (dAlpha -1 + alpha)*math.log(n)
        print "returned case 2 "+str(retValue)
        #return math.floor(retValue)
        return retValue
    
    elif ( (m >= n*(math.pow(math.log(n),2)) ) and (m <= n*(math.pow(math.log(n),3)) ) ):
        retValue = (m/n) + alpha*(math.sqrt(2*(m/n)*math.log(n)))
        print "returned case 3 "+str(retValue)
        #return math.floor(retValue)
        return retValue
    elif ( m > n*(math.pow(math.log(n),3)) ):
        secondTerm = ( math.log(math.log(n))/(2*alpha*math.log(n)))
        if(secondTerm < 0):
            secondTerm = 0
        
        retValue = (m/n) + math.sqrt( (2*(m/n)*math.log(n))*(1-  secondTerm) ) 
        print "returned case 4 "+str(retValue)
        #return math.floor(retValue)
        return retValue
    
    print "No case matching. Not possible "
    return (Aavg*currH)/B

def hyperspaceHashingModel(H, rho, N, CsByC, B, CuByC, Aavg):
    #H = round(H)
    currX= maxBallsFun(H, Aavg, B)
    #currX= Aavg
    print "currX "+str(currX) +" currH "+str(H)
    if ( (currX > 0) ):
        numNodesSubspace = N/(B/H)
        numNodesSearch = calculateExpectedNumNodesASearchGoesTo(numNodesSubspace, H, currX)
        return rho*numNodesSearch*CsByC + (1-rho) * (B/H) * CuByC
    else:
        currX = (Aavg*H)/B
        print "Not a good value "
        numNodesSubspace = N/(B/H)
        numNodesSearch = calculateExpectedNumNodesASearchGoesTo(numNodesSubspace, H, currX)
        return rho*numNodesSearch*CsByC + (1-rho) * (B/H) * CuByC
    
def Optimizer(rho, N, CsByC, B, CuByC, Aavg):
    start_pos = 12.0
    #Says one minus the sum of all variables must be zero
    cons = ({'type': 'ineq', 'fun': lambda x:  B - x}, {'type': 'ineq', 'fun': lambda x:  x-2})
    
    #opt = {'maxiter': 1, 'disp':True}
    opt = {'disp':True}

    bnds = [(1, B)]
    #Required to have non negative values
    #bnds = tuple((0,B) for x in start_pos)
    
    #result = minimize(hyperspaceHashingModel, start_pos, method='SLSQP', constraints=cons, options=opt)
    data = (rho, N, CsByC, B, CuByC, Aavg)
    result = minimize(hyperspaceHashingModel, start_pos, method='SLSQP', constraints=cons, options=opt, args = data, bounds = bnds)
    print(result.x)
    optimalH = result.x[0]
    if(optimalH > B):
        optimalH = B
    maxAttrMatching = maxBallsFun(optimalH, Aavg, B)
    
    if(maxAttrMatching > optimalH):
        exponent = maxAttrMatching/optimalH
    else:
        exponent = maxAttrMatching/optimalH
    
    print "rho "+str(rho)+" optimal H "+str(optimalH)+" maxAttrMatching "+str(maxAttrMatching)+" exponent "+ str(exponent) +"\n"
    #denominatorValue = rho*math.pow(Yc, maxAttrMatching)*math.pow(N,1-(maxAttrMatching/optimalH) )*Cs + (1-rho) * (B/optimalH) * Cu
    #T = N * C/denominatorValue
    #print "rho "+str(rho)+" optimal H "+str(optimalH)+" maxAttrMatching "+str(maxAttrMatching)+" exponent "+ str(exponent) +" throuhput "+str(T)
    
# loops through all H values to check for optimal value of H
def loopOptimizer(rho, N, CsByC, B, CuByC, Aavg):
    valueDict = {}
    optimalH  = -1.0
    minValue  = -1.0
    currH     = 1.0
    while( currH <= B ):
        currValue = hyperspaceHashingModel(currH, rho, N, CsByC, B, CuByC, Aavg)
        valueDict[currH] = currValue
        if( currH == 1.0 ):
            optimalH = currH
            minValue = currValue
        else:
            if(currValue < minValue):
                optimalH = currH
                minValue = currValue
        currH = currH + 1.0
    
    print "rho "+ str(rho)+" optimalH "+str(optimalH)+" minValue "+str(minValue)+"\n"
    

rho = 0.0
while (rho <= 1.0):
    print "###################################"
    print "rho "+ str(rho)
    #Optimizer(rho, N, CsByC, B, CuByC, Aavg)
    loopOptimizer(rho, N, CsByC, B, CuByC, Aavg)
    print "###################################"
    print "\n\n\n\n"
    rho = rho + 0.1

#Optimizer(0.0, N, CsByC, B, CuByC, Aavg)
#Optimizer(1.0, N, CsByC, B, CuByC, Aavg)
#currNumNodes = 1.0
#currH = 4.0
#currM = 2.0

#while(currNumNodes <= 36.0):
#    numSearchNodes = calculateExpectedNumNodesASearchGoesTo(currNumNodes, currH, currM)
#    
#    print "expected search nodes for "+str(currNumNodes)+" nodes "+str(numSearchNodes)
#    currNumNodes = currNumNodes + 1.0