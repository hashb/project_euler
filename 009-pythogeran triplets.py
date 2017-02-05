for x in xrange(1,340):
	for y in xrange(1,500):
		z=1000-x-y
		if x*x+y*y==z*z:
			print x,y,z,x*y*z
			