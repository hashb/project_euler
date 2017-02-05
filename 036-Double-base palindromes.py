nums=[]
for x in xrange(1,1000000):
	b = bin(x)
	x=str(x)
	if x[:]==x[::-1] and b[2:]==b[:1:-1] :
		nums.append(int(x))

print sum(nums),len(nums)