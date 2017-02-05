#open problem8.txt
page = open("problem8.txt",'r')
num = page.read()
prodx=0
for x in xrange(0,996):
	prod = int(num[x]) * int(num[x+1]) * int(num[x+2]) * int(num[x+3]) * int(num[x+4])
	if prod>prodx:
		prodx=prod
		print x,prodx