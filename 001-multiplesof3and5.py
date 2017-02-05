import math;

num = 3;
total = 0;
while num<1000 :
	if ((num % 3 == 0) or (num % 5 == 0)) :
		#print "help";
		total = total + num;
		num = num + 1;
		print num;
	else :
		num = num + 1;
print total;
