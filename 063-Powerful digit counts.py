a=[]
for x in xrange(1,1000):
	for y in xrange(1,1000):
		power = pow(y,x)
		if len(str(power))==x:
			a.append(str(power)+" "+str(x))
		elif len(str(power))>x: break

print len(set(a)),len(a)