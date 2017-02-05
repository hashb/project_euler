f=open('primes.txt','r')
primes = f.read().split(',')

def isprime(number):  
    if number!=2 and (number<=1 or number%2==0):  
        return False
    if number==3:
        return True
    check=3  
    maxneeded=number  
    while check<maxneeded+1:  
        maxneeded=number/check  
        if number%check==0:  
            return False
        check+=2  
    return True

a=[];great=0
print len(primes)
for x in xrange(0,78497):
	sums=0;i=0
	while sums<1000000:
		sums+=int(primes[x+i])
		if isprime(sums) and i>great:
			great=i
			greatSum=sums
		if i<len(primes):i+=1


print great,greatSum