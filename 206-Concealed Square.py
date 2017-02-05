def check(num):
    a=[]
    num=list(str(num))
    data=["1","2","3","4","5","6","7","8","9","0"]
    for x in xrange(0,10):
        a.append(num[2*x])
    if a==data:
        return True
    else:return False
    
number=1389026620
while number>1000000000:
    if number%10==0 and len(str(number**2))==19 :
        if check(number**2):
            print number
            break
    number-=10