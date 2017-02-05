def isprime(number):  
    if number!=2 and (number<=1 or number%2==0):  
        return False
    if number==3:
        return True
    check=3  
    maxneeded=number  
    while check<maxneeded+1:  
        maxneeded=number/check  
        if number%check==0:  
            return False
        check+=2  
    return True

def trunc(number):
    a=str(number)
    for x in xrange(0,len(a)):
        if isprime(int(a[x:])) and isprime(int(a[:len(a)-x])) :
            pass
        else :
            return False
            break
    return True

def main():
    count = 0;i = 10;nums=[]
    while count<11:
        if trunc(i) :
            print i
            nums.append(i)
            count+=1
        i+=1
    print sum(nums)
    print nums

if __name__ == '__main__':
    main()

