from itertools import permutations
a=[]
for p in permutations('0123456789'):
    # join tuple p to a string
    a.append("".join(p))

print a[1000000]