numbers = []
def sums(arr):
	total=0
	for x in xrange(0,len(arr)):
		total += pow(int(arr[x]),5)
	return total


for x in xrange(2,295245):
	a=[]
	for y in xrange(0,len(str(x))):
		a.append(str(x)[y])
	total = sums(a)
	if x == total:
		numbers.append(x)

print numbers,sum(numbers)