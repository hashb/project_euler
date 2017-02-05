digits = ['1','2','3','4','5','6','7','8','9'];n=[]
for x in xrange(1,999999):
	for y in xrange(1,10000):
		a=str(x)+str(y)+str(x*y)
		if len(a)>9:
			break
		if digits==sorted(a):
			n.append(int(x*y))
			#print x,y,a

print len(n),sum(set(n)),sum(n)

