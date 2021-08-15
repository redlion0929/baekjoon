import sys
sys.setrecursionlimit(10000)

def DFS(s, graph):
    visited[s-1] = 1
    for i in graph[s]:
        if visited[i-1] == 0:
            DFS(i,graph)
            
n, m = map(int,sys.stdin.readline().rstrip().split())
cnt = 0

graph = {}
visited = [0]*(n)
for i in range(n):
    graph[i+1] = []

for _ in range(m):
    i, j = map(int,sys.stdin.readline().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)
    
for i in range(n):
    if visited[i]==0:
        cnt+=1
        DFS(i+1,graph)
    else:
        continue
        
print(cnt)