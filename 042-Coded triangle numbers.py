def wordsFile():
	f = open('42-words.txt','r')
	words = f.read().split(',')
	f.close()
	return words

def triangular():
	a=[]
	for x in xrange(1,100000):
		tri=x*(x+1)/2
		a.append(str(tri))
	return a

def wordValues(data):
	a=[]
	for x in xrange(0,len(data)):
		sums=0
		word=data[x].replace('"','')
		for y in xrange(0,len(word)):
			sums+=ord(word[y])-64
		a.append(sums)
	return a

def main():
	total=0
	data = wordValues(wordsFile())
	triNums = triangular()
	#data=set(data)
	for x in xrange(0,len(data)):
		if str(data[x]) in triNums :
			total+=1
	print total#,data

if __name__ == '__main__':
	main()