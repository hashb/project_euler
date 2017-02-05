from __future__ import division

Onum = 100
count = 0
r=0
for x in xrange(10**10):
    Onum+=1
    num = Onum
    num = list(str(num))
    if num == sorted(num) or num[::-1] == sorted(num):
        count+1
    else: continue
print count

#if list(num1) == sorted(list(num1)): print 'increasing'
#if list(num2)[::-1] == sorted(list(num2)): print 'decreasing'
#if list(num3) != sorted(list(num3)): print "bouncy"
