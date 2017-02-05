def sum_of_factors(num):
	_sum=0
	for x in xrange(1,(num/2)+1):
		if num%x==0:
			_sum+=x
	return _sum


def main():
	num=0
	total=0
	while num<10000:
		sum_f=sum_of_factors(num)
		if sum_f!=num and num==sum_of_factors(sum_f):
			total+=num
			print num
		num+=1
	print total

if __name__ == '__main__':
	main()
