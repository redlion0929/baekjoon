import sys
t = int(sys.stdin.readline().strip())
result = []
for _ in range(t) :
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    apart = [[0 for _ in range(n)] for _ in range(k+1)]
    floor = 0
    for i in range(len(apart)):
        for j in range(len(apart[i])):
            if i==0:
                apart[i][j] = (j+1)
            else:
                for u in range(j,-1,-1):
                    apart[i][j]+= apart[i-1][u]
    print(apart[k][n-1])
