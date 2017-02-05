dec = ""
i=1
while len(dec)<1000001:
	dec +=str(i)
	#print dec
	i+=1
print int(dec[1-1])*int(dec[10-1])*int(dec[100-1])*int(dec[1000-1])*int(dec[10000-1])*int(dec[100000-1])*int(dec[1000000-1])