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
    if len(set(factors))==4 :
        return True
    else:return False
i=100
while True:
    if prime_factors(i) and prime_factors(i+1) and prime_factors(i+2) and prime_factors(i+3):
        print i
        break
    i+=1
