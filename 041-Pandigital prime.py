def isPandigital(sub):
	digits = ['1','2','3','4','5','6','7','8','9']
	sub = list(sub)
	if sorted(sub) == digits[0:len(sub)]:
		return True
	else : return False

def isprime(number):  
    if number<=1 or number%2==0:  
        return False
    check=3  
    maxneeded=number  
    while check<maxneeded+1:  
        maxneeded=number/check  
        if number%check==0:  
            return False
        check+=2  
    return True

def main():
	panPrimes=[]
	for x in xrange(123456789,1234,-1):
		if isPandigital(str(x)) and isprime(x):
			print x
			break
		#	panPrimes.append(x)
	#print max(panPrimes)

if __name__ == '__main__':
	main()