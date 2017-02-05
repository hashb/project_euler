from __future__ import division

Onum = 100
count = 0
r=0
while r != 0.99:
    Onum+=1
    num = Onum
    num = list(str(num))
    if num == sorted(num) or num[::-1] == sorted(num):
        continue
    else: count+=1
    r = count/Onum
print Onum

#if list(num1) == sorted(list(num1)): print 'increasing'
#if list(num2)[::-1] == sorted(list(num2)): print 'decreasing'
#if list(num3) != sorted(list(num3)): print "bouncy"
