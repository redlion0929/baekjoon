import sys  
INF = sys.maxsize
n, m = map(int, sys.stdin.readline().rstrip().split())    
graph = {}
result = []

D = [[INF]*n for _ in range(n)]

for i in range(n):
    graph[i+1] = []
for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)
    

for i in range(1,n+1):
    for j in graph[i]:
        D[i-1][j-1] = 1
        
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            D[i-1][j-1] = min(D[i-1][j-1], D[i-1][k-1]+D[k-1][j-1])
                
for i in range(n):
    sum = 0
    for j in range(n):
        if j==i:
            continue
        sum+=D[i][j]
        
    result.append(sum)

for i in range(n):
    if result[i]==min(result):
        print(i+1)
        break