def isLychrel(num):
	for x in xrange(0,55):
		num=str(num)
		sums=int(num)+int(num[::-1])
		if str(sums)==str(sums)[::-1]:
			return False
			break
		else:num=sums
	return True
i=0
for x in xrange(1,10000):
	if isLychrel(x):
		i+=1
	
print i