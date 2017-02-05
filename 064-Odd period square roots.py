'''
Mathematica

nonSquares = Select[Range[10000], ! IntegerQ[Sqrt[#]] &]; 
a[n_] := Length[
  Last[ContinuedFraction[Sqrt[nonSquares[[n]]]]]]; Table[
 a[n], {n, 1, Length[nonSquares]}]
'''

f = open('64 - Odd period square roots.txt','r')
data = map(int,f.read().split(','))
count=0
for x in data:
    if x%2 !=0: count+=1

print count