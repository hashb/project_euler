from math import factorial
def combination(n,k):
    numerator=factorial(n)
    denominator=(factorial(k)*factorial(n-k))
    answer=numerator/denominator
    return answer
i=0;a=[]
for x in xrange(1,101):
    for y in xrange(1,x):
        b=combination(x,y)
        if b>=1000000:
            a.append(b)
            print x,y
            i+=1
print i
#print len(set(a))