import math
from scipy.optimize import fsolve

rho     = 0.5
Yc      = 1.0
N       = 10.0
Cs      = 100.0
B       = 50.0
Cu      = 1.0
Aavg    = 10.0

def dAlphsFunc(x, c):
    return 1.0 + x * (math.log(c) - math.log(x) + 1) - c

def solveDAlpha(c):
    data = (c)
    res = fsolve(dAlphsFunc, 1.0, args=data)
    
    for i in range(len(res.x)):
        if(res.x[i] > c):
            return res.x[i]
    print "dAlpha return -1"
    return -1

def maxBallsFun(currH):
    global Aavg
    global B
    
    m = Aavg
    n = math.ceil(B/currH)
    print "currH "+str(currH) + " n " + str(n)
    alpha = 1
    if ( n== 1):
        return Aavg
    
    if ( (m > 0) and (m < n*math.log((n)) ) ):
        logNlogNByM = math.log( (n * math.log(n))/m )
        retValue = (math.log(n)/logNlogNByM)*( 1+alpha * (math.log(logNlogNByM)/logNlogNByM) )
        print "returned case 1 "+str(retValue)
        
        return math.floor(retValue)
    elif ( (m >= n*math.log((n))) and m < n*math.pow(math.log(n),2) ):
        c = m/( n*math.log(n) )
        dAlpha = solveDAlpha(c)
        #dAlpha = 1
        retValue = (dAlpha -1 + alpha)*math.log(n)
        print "returned case 2 "+str(retValue)
        return math.floor(retValue)
    elif ( (m >= n*(math.pow(math.log(n),2)) ) and (m <= n*(math.pow(math.log(n),3)) ) ):
        retValue = (m/n) + alpha*(math.sqrt(2*(m/n)*math.log(n)))
        print "returned case 3 "+str(retValue)
        return math.floor(retValue)
    elif ( m > n*(math.pow(math.log(n),3)) ):
        retValue = (m/n) + math.sqrt( (2*(m/n)*math.log(n))*(1- ( math.log(math.log(n))/(2*alpha*math.log(n))) ) ) 
        print "returned case 4 "+str(retValue)
        return math.floor(retValue)
    
    print "No case matching. Not possible "
    return Aavg/currH


currH = 10
while (currH <= 50):
    result = maxBallsFun(currH)
    exponent = (result*1.0)/currH
    print "result "+str(currH)+" "+str(result)+" "+str(exponent) +"\n"
    currH = currH + 1