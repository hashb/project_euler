
import math

def no_factors(num):
	factors=1
	y=int(math.sqrt(num))+1
	for x in xrange(2,y):
		power=0
		while num%x==0:
			num=num/x
			power=power+1
		factors=factors*(power+1)
	if num>1:
		factors=factors*2
	return factors



def main():
	factors=1
	num=1
	while factors<500:
		total=num*(num+1)/2
		factors=no_factors(total)
		print total,factors,num
		num=num+1
		

	

if __name__ == '__main__':
	main()