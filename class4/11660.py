import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
table = [[0 for i in range(n + 1)] for i in range(n + 1)]

for i in range(1,n+1):
    l = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(1,len(l)+1):
        table[i][j] = table[i-1][j]+table[i][j-1]-table[i-1][j-1]+l[j-1]
        
for _ in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().rstrip().split())
    print(table[y2][x2]-table[y1][