a=[]
for x in xrange(1,1000000):
	num = sorted(list(str(x**3)))
	a.append(num)
	if a.count(num)==5:
		print (a.index(num)+1)**3
		break
