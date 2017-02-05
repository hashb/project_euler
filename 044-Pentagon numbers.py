import math
def penta():
	a=[]
	for x in xrange(1,10000):
		pen = x*(3*x - 1)/2
		a.append(str(pen))
	return a

def ispenta(t):
	if (1+math.sqrt(1**2+4*3*2*t))/(2*3) % 1 == 0:
		return True
	else : return False

pentagonal=penta();data=[]
for x in xrange(1,len(pentagonal)):
	for y in xrange(1,len(pentagonal)):
		sums=int(pentagonal[x])+int(pentagonal[y])
		diff=int(pentagonal[x])-int(pentagonal[y])
		if ispenta(sums) and ispenta(abs(diff)):
				print diff
				break
			#data.append(abs(diff))

#print data