f=open('primes.txt','r')
primes = f.read().split(',')
import math
def isprime(number):  
	if number!=2 and (number<=1 or number%2==0):  
		return 0
	if number==3:
		return 1
	check=3  
	maxneeded=number  
	while check<maxneeded+1:  
		maxneeded=number/check  
		if number%check==0:  
			return 0
		check+=2  
	return 1
a=[]
def goldbach(num):
	sums=0;x=0
	while sums<num:
		while sums<=num:
			if num>int(primes[x]):
				i = math.sqrt((num-int(primes[x]))/2)

			if (int(primes[x]) + (2 * int(i)**2)) > num:
				break			
			sums = int(primes[x]) + (2 * int(i)**2)
			#print sums,primes[x],i
			if sums==num or sums+1==num or sums-1==num:
				a.append(str(primes[x])+' + 2*'+str(int(i))+'(+or-)^2')
				return True
			else : print num ;break
		x+=1
	print num
	return False
x=9
#print goldbach(27)
while True:
	if x%2!=0 and isprime(x)==0:
		if goldbach(x):
			x+=1
		else : break
	else:x+=1