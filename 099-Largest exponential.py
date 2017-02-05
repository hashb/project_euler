from math import log

f = open('099_base_exp.txt','r')
data = f.read().split('\n')

maxval = 1
line = 0
for pair in data:
    line+=1
    pair = map(int,pair.split(','))
    val = pair[1]*log(pair[0])
    if val > maxval :
        #print line,maxval
        maxval = val
        maxline = line
print maxline