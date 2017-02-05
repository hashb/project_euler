from itertools import permutations

def perms():
	data = permutations('0123456789')
	newData=[]
	data = map(list,data)
	for x in xrange(0,len(data)):
		newData.append(''.join(data[x]))
	return newData

def divisionTest(data):
	primes=[2,3,5,7,11,13,17]
	for x in xrange(1,8):
		if int(data[x:x+3])%primes[x-1] == 0 :
			pass
		else:
			return False
			break
	return True

def main():
	data = perms()
	sums=[]
	print len(data)
	for x in xrange(0,len(data)):
		if divisionTest(data[x]) :
			sums.append(int(data[x]))
	print sum(sums)

if __name__ == '__main__':
	main()
