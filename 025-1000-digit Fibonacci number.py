num1 = 1;
num2 = 2;
total = 0;
str_len=0
index=3
while str_len<1000 :
	new = num1 + num2;
	num1 = num2;
	num2 = new;
	index+=1
	str_len=len(str(new))

print num1,"\n",index,str_len

