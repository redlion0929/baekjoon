import sys
from collections import deque 

n, m = map(int, sys.stdin.readline().rstrip().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]
miro = []
visit = deque()
visited = [[False]*m for _ in range(n)]

for _ in range(n):
    line = sys.stdin.readline().rstrip()
    miro.append([])
    for i in line:
        miro[-1].append(int(i))

visit.append((0,0))
visited[0][0] = True

while True:
    coor = visit.popleft()
    i = coor[0]
    j = coor[1]
    
    for u in range(4):
        if (((i+dy[u])<=(n-1)) & ((i+dy[u])>=0)& ((j+dx[u])<=(m-1)) & ((j+dx[u])>=0)):
            if ((miro[i+dy[u]][j+dx[u]]==1) & (visited[i+dy[u]][j+dx[u]]==False)):
                miro[i+dy[u]][j+dx[u]] = miro[i][j]+1
                visit.append((i+dy[u],j+dx[u]))
                visited[i+dy[u]][j+dx[u]]=True
        
    if ((i==n-1) & (j==m-1)):
        print(miro[i][j])
        exit()