one = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200]
two = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]
five = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]
ten = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
twenty = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
fifty = [0, 50, 100, 150, 200]
hundred = [0, 100, 200]

def lame():	
	sums=0
	for s in xrange(0,3):
		for x in xrange(0,len(fifty)):
			for y in xrange(0,len(twenty)):
				for z in xrange(0,len(ten)):
					for p in xrange(0,len(five)):
						for q in xrange(0,len(two)):
							for r in xrange(0,len(one)):
								if 200 == hundred[s] + fifty[x] + twenty[y] + ten[z] + five[p] + two[q] + one[r] :
									sums +=1
									#print sums

	print sums+1



def iteration():
    count = 0
    for i in range(0, 2):
        for j in range(0, 3 - 2 * i):
            for k in range(0, 5 - 2 * j  - 4 * i):
                for l in range(0, 11 - 5 * j - 10 * i):
                    for m in range(0, 21 - 2 * l - 5 * k - 10 * j):
                        for n in range(0, 41 - 2 * m - 4 * l - 10 * k - 20 * j):
                            for o in range(0, 101 - 5 * m - 10 * l - 50 * j - 100 * i):
                                for p in range(0, 201 - 2 * o - 5 * n - 10 * m - 20 * l - 50 * k - 100 * j - 200 * i):
                                    sum_ = i * 200 + j * 100 + k * 50  + 20 * l + 10 * m  + 5 * n + 2 * o + p
                                    if sum_ == 200:
                                        count += 1
    print  count     

if __name__ == '__main__':
	iteration()