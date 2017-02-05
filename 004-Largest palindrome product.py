

def palindrome(num):
	n = str(num)
	#print n
	if n == n[::-1]:
		print num

def main():
	num1 = 100
	num2 = 100
	while num1<1000 :
		while num2<1000:
			prod = num1*num2
			palindrome(prod)
			num2 = num2 +1

		num1 = num1 +1
		num2 = 100

if __name__ == '__main__':
	main()