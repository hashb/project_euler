great = 0
for x in xrange(1,100):
	for y in xrange(1,100):
		power = pow(x,y)
		d = list(str(power))
		d = map(int,d)
		d = sum(d)
		if d>great:
			great=d

print great