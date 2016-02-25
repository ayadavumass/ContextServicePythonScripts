import math
from scipy.optimize import minimize
from scipy.optimize import fsolve

#result = minimize(f, [1])
#print(result.x)
rho     = 0.1
Yc      = 1.0
N       = 10.0
Cs      = 100.0
B       = 50.0
Cu      = 20.0
Aavg    = 10.0
C       = 1000.0

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
    return Aavg/currH

def hyperspaceHashingModel(H, rho, Yc, N, Cs, B, Cu, Aavg):
    #H = round(H)
    currX= maxBallsFun(H, Aavg, B)
    #currX= Aavg
    print "currX "+str(currX) +" currH "+str(H)
    if ( (currX > 0) ):
        return rho*math.pow(Yc, currX)*math.pow(N,1-(currX/H) )*Cs + (1-rho) * (B/H) * Cu
    else:
        currX = Aavg/H
        print "Not a good value "
        return rho*math.pow(Yc, currX)*math.pow(N,1-(currX/H) )*Cs + (1-rho) * (B/H) * Cu


def Optimizer(rho, Yc, N, Cs, B, Cu, Aavg, C):
    start_pos = 10
    #Says one minus the sum of all variables must be zero
    cons = ({'type': 'ineq', 'fun': lambda x:  B - x}, {'type': 'ineq', 'fun': lambda x:  x-2})

    #opt = {'maxiter': 1, 'disp':True}
    opt = {'disp':True}

    bnds = [(1, B)]
    #Required to have non negative values
    #bnds = tuple((0,B) for x in start_pos)

    #result = minimize(hyperspaceHashingModel, start_pos, method='SLSQP', constraints=cons, options=opt)
    data = (rho, Yc, N, Cs, B, Cu, Aavg)
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

    denominatorValue = rho*math.pow(Yc, maxAttrMatching)*math.pow(N,1-(maxAttrMatching/optimalH) )*Cs + (1-rho) * (B/optimalH) * Cu
    T = N * C/denominatorValue
    print "rho "+str(rho)+" optimal H "+str(optimalH)+" maxAttrMatching "+str(maxAttrMatching)+" exponent "+ str(exponent) +" throuhput "+str(T)
    
    
rho = 0.0
while (rho <= 1.0):
    print "rho "+ str(rho)+"\n\n"
    Optimizer(rho, Yc, N, Cs, B, Cu, Aavg, C)
    rho = rho + 0.1