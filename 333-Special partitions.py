f=open("primes.txt","r")
primes=f.read().split(",")
f.close()

def Partition(num):
	i=0
	for p in xrange(0,20):
		for q in xrange(0,20):
			for x in xrange(1,20):
				for y in xrange(1,20):
					if num==(pow(2,x)*pow(3,p))+(pow(2,q)*pow(3,y)):
						i+=1
						#print x,y
					if i>1:
						return False
	if i==0:return False
	else:return True

a=0
for x in primes:
	#print primes[x]
	if Partition(int(x)):
		a+=int(x)
		#print primes[x]

print a