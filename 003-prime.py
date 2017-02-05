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
    print number  

def main():
    num = 600851475143
    i = 2;
    while i<300425737572 :
        if num % i == 0 :
            isprime(i)
        i = i+1

if __name__ == '__main__':
    main()
