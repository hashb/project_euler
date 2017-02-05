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
    psum = 5
    while x!=2000000 :
        i = isprime(x)
        #print i,x
        if i==1:
            psum = psum + x
        x = x + 1
    print psum

if __name__ == '__main__':
    main()