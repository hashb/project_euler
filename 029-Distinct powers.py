a=[]
for x in xrange(2,101):
	for y in xrange(2,101):
		a.append(pow(x,y))


print "no repeats :",len(set(a)),"repeats :",len(a)