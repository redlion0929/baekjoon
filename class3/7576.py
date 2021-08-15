import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

m, n = map(int,sys.stdin.readline().rstrip().split())
tomato = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
q = deque()

def ripe():
    while q:
        i,j = q.popleft()
        visited[i][j] = True
        for u in range(4):
            y = i+dy[u]
            x = j+dx[u]
            if ((0<=x<m) & (0<=y<n)):
                if ((tomato[y][x]==0) & (visited[y][x] == False)):
                    q.append([y,x])
                    tomato[y][x] = tomato[i][j] + 1
                
                
for i in range(len(tomato)):
    for j in range(len(tomato[i])):
        if tomato[i][j] == 1:
            q.append([i,j])
ripe()

days = 0
for i in range(len(tomato)):
    for j in range(len(tomato[i])):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        days = max(days,tomato[i][j])
print(days-1)