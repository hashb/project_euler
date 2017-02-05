from itertools import permutations
def isprime(number):  
    if number<=1 or number%2==0:  
        return False
    check=3  
    maxneeded=number  
    while check<maxneeded+1:  
        maxneeded=number/check  
        if number%check==0:  
            return False
        check+=2  
    return True

def primePerms(data):
    data = permutations(data)
    newData=[]
    data = map(list,data)
    for x in xrange(0,len(data)):
        if '0' in data[x]:
            return newData
        digit = ''.join(data[x])
        if isprime(int(digit)):
            newData.append(digit)
    newData=sorted(newData)
    return newData

def seq(data):
    for x in xrange(0,len(data)-2):
        for y in xrange(x,len(data)-1):
            for z in xrange(y,len(data)):
                diff1=int(data[x])-int(data[y])
                diff2=int(data[y])-int(data[z])
                if diff1==diff2 and diff1!=0 :
                    return str(data[x])+str(data[y])+str(data[z])

a=[]
for x in xrange(1000,10000):
    new= primePerms(str(x))
    a.append(seq(new))

print set(a)