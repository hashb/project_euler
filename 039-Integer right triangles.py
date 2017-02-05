import collections
a=[]

for x in xrange(1,500):
	for y in xrange(1,500):
		for z in xrange(1,500):
			if x*x + y*y == z*z and x+y+z<1000:
				#print x+y+z
				a.append(z+y+x)
x=collections.Counter(a)
print(x.most_common())
#print a