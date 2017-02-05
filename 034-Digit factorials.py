"409113"
import math
def digitFactorialSum(num):
	num=list(str(num))
	total=0
	for x in xrange(0,len(num)):
		total += math.factorial(int(num[x]))
	return total

nums=[]
for x in xrange(10,409113):
	if digitFactorialSum(x) == x :
		nums.append(int(x))

print sum(nums)