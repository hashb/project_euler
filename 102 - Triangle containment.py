from __future__ import division

f = open('102_triangles.txt','r')
triangles = f.read().split('\n')
total=0
for triangle in triangles:
    data = map(int,triangle.split(','))

    A = [data[0],data[1]]
    B = [data[2]-data[0] , data[3]-data[1]]
    C = [data[4]-data[0] , data[5]-data[1]]

    a = -((A[0]*C[1])-(A[1]*C[0]))/((B[0]*C[1])-(B[1]*C[0]))
    b =  ((A[0]*B[1])-(A[1]*B[0]))/((B[0]*C[1])-(B[1]*C[0]))

    if a>0 and b>0 and a+b<1 :
        total+=1

print total