from __future__ import division

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

def phi(n):
    res = n
    Nfac = prime_factors(n)
    for f in Nfac:
        res = res*(1 - 1/f)
    return res

a=[]
minval=100000000000
for x in xrange(2,10**7):
    P = phi(x)
    if sorted(list(str(int(P)))) == sorted(list(str(x))):
        mini = x/P
        if mini<minval: 
            minval=mini
            minimum_n = x
        a.append(x)

print a, len(a), minimum_n