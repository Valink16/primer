from time import time
def primeList(limit,getTime=False):
    if(getTime):
        s=time()
    primes=[2,3]
    for act in range(5,limit,2):
        isPrime=True
        for i in range(3,act):
            if(act%i==0):
                isPrime=False
                break
        if(isPrime):
            primes.append(act)
    if(getTime):
        e=time()
        return {"primes":primes,"time":e-s}
    return {"primes":primes}
