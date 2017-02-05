"""
16/64 = 1/4
26/65 = 2/5
19/95 = 1/5
49/98 = 1/2

"""
def stC(num1,num2):
	flag=0
	a = list(str(num1));b=list(str(num2))
	for x in xrange(0,len(a)):
		for y in xrange(0,len(b)-1):
			if a[x]==b[y] :
				flag=1
				del a[x],b[y]
	if flag==1:
		return [a[0],b[0]]
	else:return 0

def isprime(number):  
	if number<=1 or number%2==0:  
		return False
	check=3  
	maxneeded=number  
	while check<maxneeded+1:  
		maxneeded=number/check  
		if number%check==0:  
			return False
		check+=2  
	return True

def kautilya():
	a=[]
	b=[]
	for x in range(1,10):
	    for y in range(x,10):
	        num=float(9)*x*y/(10*x-y)
	        if int(num) == num and x/y < 1 and num<10:
	            a.append(x)
	            b.append(y)
	            print num, x, y, str(10*x+num)+'/'+str(y+10*num), str(x)+'/'+str(y)

	numerator = a[0]*a[1]*a[2]*a[3]
	denominator = b[0]*b[1]*b[2]*b[3]
	print numerator,denominator,denominator/numerator

def nami_And_OR_Or_lobo():
	for x in xrange(11,99):
		if x%10==0:
			continue
		for y in xrange(x+1,99):
			if y%10==0:
				continue
			#print x,y
			div=stC(x,y)
			if div!=0:
				if float(x)/float(y)==float(div[0])/float(div[1]) and x/y<1 :
					print "result",x,y,div

if __name__ == '__main__':
	nami_And_OR_Or_lobo()