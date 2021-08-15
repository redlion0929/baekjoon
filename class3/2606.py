import sys
from collections import deque

V = int(sys.stdin.readline().rstrip())
E = int(sys.stdin.readline().rstrip())

graph = {}

for i in range(1,V+1):
    graph[i] = []
    
visited = [0] * (V+1)
    
for _ in range(E):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)
    
def BFS(graph, start_node):
    queue = deque([start_node])
    visited[start_node] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i]==0:
                queue.append(i)
                visited[i]=1
                
BFS(graph, 1)
print(visited.count(1)-1)