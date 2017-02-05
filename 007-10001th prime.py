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

def main() :
    flag = 0
    x = 2
    while flag != (10001-2) :
        i = isprime(x)
        #print i,x
        flag = flag + i
        x = x + 1
    print x-1

if __name__ == '__main__':
    main()