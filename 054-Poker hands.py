#C - Club
#S - Spade
#D - Diamond
#H - Heart
data = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def highCard(a11,a22):
	#print a11,a22
	p1=max(a11);p2=max(a22)
	if p1>p2 : return 1
	if p1<p2 : return 0
	if p1 == p2 :
		a11.remove(max(a11))
		a22.remove(max(a22))
	#	print a11,a22
	return highCard(a11,a22)


def onePair(a):
	if len(set(a))== 4:
		for x in set(a):
			if a.count(x)==2:
				return 2+data.index(x)
	else:return 0

def twoPair(a):
	b=[];rule=[1,2,2]
	for x in set(a):
		b.append(a.count(x))
	if sorted(b)==rule:
		return 3
	else:return 0

def threeOfaKind(a):
	b=[];rule=[1,1,3]
	for x in set(a):
		b.append(a.count(x))
	if sorted(b)==rule:
		return 4
	else:return 0

def straight(a):
	for x in xrange(0,9):
		if sorted(a)==sorted(data[x:x+5]):
			return 5
	return 0


def flush(b):
	if len(set(b))==1:
		return 6
	else:return 0

def fullHouse(a):
	b=[];rule=[2,3]
	for x in set(a):
		b.append(a.count(x))
	if sorted(b)==rule:
		for x in set(a):
			if a.count(x)==3:
				return 7+13+data.index(x)
		#return 7
	else:return 0

def fourOfaKind(a):
	b=[];rule=[1,4]
	for x in set(a):
		b.append(a.count(x))
	if sorted(b)==rule:
		return 20+data.index()
	else:return 0

def straightFlush(a,b):
	if len(set(a))==1 :
		for x in xrange(0,9):
			if sorted(b)==sorted(data[x:x+5]) :
				return 49
		return 0
	else:return 0

def royalFlush(a):
	royal = ["A","J","K","Q","T"]
	if sorted(a)==royal:
		return 50
	else:return 0

def pokerTests(cards):
	a=[];b=[];res=[]
	for x in cards:
		#print x,x[0]
		a.append(str(x[0]))
		b.append(str(x[1]))
	res.append(onePair(a));res.append(twoPair(a));res.append(threeOfaKind(a));
	res.append(straight(a));res.append(flush(b));res.append(fullHouse(a));
	res.append(fourOfaKind(a));res.append(straightFlush(a,b));res.append(royalFlush(a))
	return res


def main():
	player1=0
	f = open("poker.txt","r")
	games = f.read().split("\n")
	for x in games:
		hands = x.split(" ")
		hand1=hands[:5]
		hand2=hands[5:10]
		#print hand1
		#break
		res1=pokerTests(hand1)
		res2=pokerTests(hand2)
		if max(res1)>max(res2) :
			player1+=1
		if max(res1)==max(res2) :
			a1=[];a2=[]
			for x in xrange(0,len(hand1)):
				a1.append(data.index(hand1[x][0]))
				a2.append(data.index(hand2[x][0]))
			player1+=highCard(a1,a2)
	print player1


if __name__ == '__main__':
	main()