import sys
from collections import deque
m, n, h = map(int,sys.stdin.readline().rstrip().split())

dz = [-1,1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
q = deque()

def ripe():
    while q:
        i,j,k = q.popleft()
        visited[i][j][k] = True
        for u in range(6):
            z = i+dz[u]
            y = j+dy[u]
            x = k+dx[u]
            if ((0<=z<h) & (0<=y<n) & (0<=x<m)):
                if ((tomato[z][y][x] == 0) & (visited[z][y][x]==False)):
                    tomato[z][y][x] = tomato[i][j][k]+1
                    visited[z][y][x] = True
                    q.append([z,y,x]) //i+dz[u]를 z로 바꿈
    
tomato = [[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

for i in range(len(tomato)):
    for j in range(len(tomato[i])):
        for k in range(len(tomato[i][j])):
            if tomato[i][j][k]==1:
                q.append([i,j,k])
ripe()

days = 0

for i in range(len(tomato)):
    for j in range(len(tomato[i])):
        for k in range(len(tomato[i][j])):
            if tomato[i][j][k]==0:
                print(-1)
                exit()
            days = max(days,tomato[i][j][k])
print(days-1)