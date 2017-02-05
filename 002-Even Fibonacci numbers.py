num1 = 1;
num2 = 2;
total = 0;
while num2<4000000 :
	if (num2 % 2 == 0) :
		total = total + num2;
		print total;

	new = num1 + num2;
	num1 = num2;
	num2 = new;
	#print new

