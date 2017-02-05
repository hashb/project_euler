#days=["sun","mon","tue","wed","thu","fri","sat"]


def dow(y,m,d):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y -= m < 3
    return (y + y/4 - y/100 + y/400 + t[m-1] + d ) % 7

def main():
	months=[29,31,28,31,30,31,30,31,31,30,31,30,31]
	total = 0
	for y in xrange(1901,2001):
		for m in xrange(1,13):			
			day = dow(y,m,1)
			if day==0:
				total = total +1

	print y,m,total

if __name__ == '__main__':
	main()
				
			
