def sumsquare() :
	sums = 0
	for x in xrange(1,101):
		sums = sums + x
		new_sums = sums*sums
	return new_sums

def squaresum() :
	ssum=0
	for x in xrange(1,101):
		ssum = ssum + (x*x)
	return ssum

def main():
	new_sums=sumsquare()
	ssum=squaresum()
	res = ssum-new_sums
	print res
	print ssum
	print new_sums

if __name__ == '__main__':
	main()
