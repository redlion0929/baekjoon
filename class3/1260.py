import sys
from collections import deque
V, E, S = map(int, sys.stdin.readline().rstrip().split())

graph = {}
visited_BFS = [0]*(V+1)
visited_DFS = [0]*(V+1)
for i in range(V+1):
    graph[i] = []

for _ in range(E):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)
    
def BFS(graph, S):
    q = deque([S])
    visited_BFS[S] = 1
    print(S, end = " ")
    while q:
        v = q.popleft()
        for i in sorted(graph[v]):
            if visited_BFS[i]==0:
                q.append(i)
                print(i, end = " ")
                visited_BFS[i]=1
                
def DFS(graph, S):
    visited_DFS[S] = 1
    print(S, end = " ")
    for i in sorted(graph[S]):
        if visited_DFS[i]==0:
            DFS(graph,i)
            
DFS(graph,S)
print()
BFS(graph,S)
            