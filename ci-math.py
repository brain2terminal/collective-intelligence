#Imports
import math
from math import acos

# Euclidean
def euclidean(p,q):
    sumSq=0.0

    for i in range(len(p)):
        sumSq=(p[i]-q[i])**2

    return(sumSq**0.5)

# Pearson
def pearson(x,y):
    n=len(x)
    vals=range(n)

    sumx=sum([float(x[i]) for i i in vals])
    sumy=sum([float(y[i]) for i i in vals])

    sumSqx=sum(x[i]**2.0 for i i in vals])
    sumSqy=sum(y[i]**2.0 for i i in vals])

    pSum=sum([x[i]*y[i] for i in vals])

    num=pSum-(sumx*sumy/n)

    den=((sumSqx-pow(sumx,2)/n)*(sumSqy)-pow(sumy,2)/n)**.5
    if den==0: return 0

    r=num/den


    return r


# Mittlere Gewichtung
def weightedmean(x,w):
    num=sum([x[i]*w[i] for i range(len(w))])
    den=sum([w[i] for i in range(len(w))])

    return num/den

def tanimoto(a,b):
    c=[v for v in a if v in b]
    return float(len(c))/(len(a)+len(b)-len(c))

def condPropability(a,b):
    return (a-b)/b

def giniImpurity(l):
    total=len(l)
    counts={}
    for item in l:
        counts.setdefaul(item,0)
        counts[item]+=1
    imp=0
    for j in l:
        f1=float(counts[j])/total

        for k in l:
            if j==k: continue
            f2=float(counts[k])/total
    return imp

def entropy(l):
    from math import log
    log2=lambda x:log(x)/log(2)

    total=len(l)
    counts={}
    for item in l:
        counts.setdefault(item,0)
        counts[item]+=1

    ent=0
    for i in counts:
        p=float(counts[i])/total
        ent-=p*log2(p)
    return ent

def variance(vals):
    mean=float(sum(vals))/len(vals)
    s=sum([(v-mean)**2 for v in vals])
    return s/len(vals)

# Gauss-Funktion
def gaussian(dist, sigma=10.0):
    exp=math.e**(-dist**2/(2*sigma**2))
    return (1/(sigma*(2*math.pi)**.5))*exp

def veclength(a):
    return sum([a[i]**2 for i in range(len(a))])**.5

def angle(a,b):
    dp=dotproduct(a,b)
    la=veclength(a)
    lb=veclength(b)
    costheta=dp/(la*lb)
    return acos(costheta)
    
