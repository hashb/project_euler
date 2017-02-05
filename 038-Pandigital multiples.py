def mult(num):
	length=0;x=1;numbers=''
	while length!=9:
		prod = num * x
		length=length+len(str(prod))
		numbers += str(prod)
		x+=1
		if length>9:
			break
	return numbers
great=0;digits = ['1','2','3','4','5','6','7','8','9']
for x in xrange(1,10000):
	num = mult(x)
	if digits==sorted(list(num)) and num>great :
		great=num;greatx=x

print great,greatx

