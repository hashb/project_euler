def circle(num):
	num=list(str(num));temp=num[0];new=[]
	for x in xrange(1,len(num)):
		new.insert(x+1,num[x])
	new.insert(len(num),temp)
	return int(''.join(new))


def isprime(number):  
    if number!=2 and (number<=1 or number%2==0):  
        return False
    if number==3:
        return True
    check=3  
    maxneeded=number  
    while check<maxneeded+1:  
        maxneeded=number/check  
        if number%check==0:  
            return False
        check+=2  
    return True
a=[]
for x in xrange(1,1000000):
	num=x;flag=0
	while flag<len(str(x)):
		if isprime(num):
			#print num
			num=circle(num)
			flag+=1
		else : break
	if flag==len(str(x)):
		a.append(x)

print len(set(a))
#zeros are not counted
c=135
for x in xrange(1,135):
	if '0' in str(a[x]):
		c-=1
print c