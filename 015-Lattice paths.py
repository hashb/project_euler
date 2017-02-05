n = 20 

g = range(n+1)
g[0] = [[0,1]]
for i in range(1,n+1):
        g[i] = range(1,i+2)
        if i > 1:
                for j in range(1,i):
                        g[i][j] = g[i-1][j] + g[i][j-1]
        g[i][i] = g[i][i-1] * 2

print g[n][n]