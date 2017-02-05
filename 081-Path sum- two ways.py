f=open("matrix.txt","r")
data=[]
a = f.read().split("\n")
for x in a : data.append(x.split(","))
print len(data)
i,j,total=79,79,7981

def addEdges():
	for x in xrange(1,80):
		data[0][x]=int(data[0][x-1])+int(data[0][x])
		data[x][0]=int(data[x-1][0])+int(data[x][0])
	return data

data = addEdges()

for x in xrange(1,80):
    for y in xrange(1,80):
        sum1=int(data[x-1][y])+int(data[x][y])
        sum2=int(data[x][y-1])+int(data[x][y])
        if sum1>sum2:
            data[x][y]=sum2
        else:data[x][y]=sum1

print data[79][79]