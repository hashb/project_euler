from fractions import Fraction as fn 
data = [1,2,1,1,4,1,1,6,1,1,8,1,1,10,1,1,12,1,1,14,1,1,
    16,1,1,18,1,1,20,1,1,22,1,1,24,1,1,26,1,1,28,1,1,
    30,1,1,32,1,1,34,1,1,36,1,1,38,1,1,40,1,1,42,1,1,
    44,1,1,46,1,1,48,1,1,50,1,1,52,1,1,54,1,1,56,1,1,
    58,1,1,60,1,1,62,1,1,64,1,1,66,1,1]

def genfrac(n,i):
    #print n
    new = data[i::-1]
    
    if (n-1)>0:
        #print n+1,new,new[n]
        return new[n] + fn(1,genfrac(n-1,i))
    else: return new[1]

frac = 2 + fn(1,genfrac(99,99))

print sum(map(int,list(str(frac.numerator))))