from __future__ import division
def numbers(x):
    if x%2==0: return []
    upR = (x-1)**2 - (x-2)
    upL = (x-1)**2 + 1
    downL = (x-1)**2 + x 
    downR = x*x
    return [upR,upL,downL,downR]

def main():
    r = 1
    nums=[]
    length=1
    f = open('PRIMES/primes1m.txt','r')
    f1 = open('PRIMES/primes2m.txt','r')
    f2 = open('PRIMES/primes3m.txt','r')
    f3 = open('PRIMES/primes4m.txt','r')
    primes = map(int,f.read().split(',')) + map(int,f1.read().split(',')) + map(int,f2.read().split(',')) + map(int,f3.read().split(','))
    while r>0.1:
        nums = list(set(nums + numbers(length)))
        nums_Primes = list(set(nums)&set(primes[2:]))
        r = len(nums_Primes)/len(nums)
        if r==0.0:r=1
        #print 'ratio',r,'side length',length,'nums lenght:',len(nums),'nums_Primes length:',len(nums_Primes)#,'nums:',sorted(nums)
        
        #if length==8:exit()
        length+=1
    print length-1

if __name__ == '__main__':
    main()