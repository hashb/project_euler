top=0
for n in xrange(2,1000000):
	i=0
	o_n=n
	while n>1:
		if n%2==0:
			n=n/2
			i=i+1
		else:
			n=(3*n)+1
			i=i+1
	if i>top:
		top=i
		greatest=o_n

print greatest



