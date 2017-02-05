from fractions import Fraction as fn
import sys
sys.setrecursionlimit(10000)
i,count  = 0,0
def genfrac(n):
    #print n
    if (n-1)>0:
        return 2 + fn(1,genfrac(n-1))
    else: return 2

#print 1 + fn(1,genfrac(3))
while i<1001:
    frac = 1 + fn(1,genfrac(i))
    #print frac
    #if i == 5 : exit()
    if len(str(frac.numerator)) > len(str(frac.denominator)):
        print i
        count+=1
    i+=1
print count

