def isprime(number):  
    if number<=1 or number%2==0:  
        return 0  
    check=3  
    maxneeded=number  
    while check<maxneeded+1:  
        maxneeded=number/check  
        if number%check==0:  
            return 0  
        check+=2  
    return 1


def main():
	num =4
	f=open('primes.txt','a')
	while num<10000:

		check = isprime(num)
		if check==1:

			f.write(str(num)+'\n')
		num=num+1
	f.close()

if __name__ == '__main__':
	main()
