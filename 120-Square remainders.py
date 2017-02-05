def bad():	
	sums=0
	for a in xrange(3,1001):
		great=0
		for n in xrange(1,1500):
			r = (pow((a-1),n)+pow((a+1),n)) % a**2
			#b.append(r)
			if r>great:
				great=r
		sums+=great

	print sums

def good():
	print sum((a-1)/2*a*2 for a in range(3, 1001))

if __name__ == '__main__':
	good()