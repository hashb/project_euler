def downR():
	sums=0
	for x in xrange(2,1001):
		if x%2==0:
			sums += x*x - (x-1)
	return sums

def downL():
	sums=0
	for x in xrange(2,1001):
		if x%2==0:
			sums += x*x + 1
	return sums

def upR():
	sums=0
	for x in xrange(2,1002):
		if x%2!=0:
			sums += x*x
	return sums

def upL():
	sums=0
	for x in xrange(2,1001):
		if x%2==0:
			sums += x*x + (x+1)
	return sums

def main():
	sumDR=downR()
	sumDL=downL()
	sumUR=upR()
	sumUL=upL()
	print "total : ",sumUL+sumUR+sumDL+sumDR+1

if __name__ == '__main__':
	main()