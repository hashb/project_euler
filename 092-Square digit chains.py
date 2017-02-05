def squaresOfDigits(number):
	sums=0
	number=map(int,number)
	for x in number:
		sums+=pow(x,2)
	return sums
i=0
for x in xrange(1,10**7):
	num=x
	#print x
	while num!= 1 or 89:
		num=squaresOfDigits(str(num))
		if num==89:
			i+=1
			break
		elif num==1:break

print i