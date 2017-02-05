import re

for x in xrange(1,51):
	wri = open('primes'+ str(x) + 'm.txt', 'a')
	f = open("primes" + str(x) + ".txt", 'r')
	#print x
	data = f.readlines()[2:]
	for y in data:
		for b in re.findall( r'\d+',y):
			#print b
			#exit()
			wri.write(str(b) + ',')
