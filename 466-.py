a=[]

for x in xrange(1,65):
	for y in xrange(1,10**16):
		if x==y or x<y:
			a.append(x*y)
		else : pass

print len(set(a))