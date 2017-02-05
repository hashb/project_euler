import math
n = 40766
while 1:
    t = n*(n+1)/2
    if (1+math.sqrt(1**2+4*3*2*t))/(2*3) % 1 == 0:
        if (1+math.sqrt(1**2+4*2*t))/(2*2) % 1 == 0:
            print n*(n+1)/2
            break
    n += 1