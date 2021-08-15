import sys
n,m = map(int,sys.stdin.readline().rstrip().split())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

paper = []
maxx = 0

def dfs(i,j,summ,cnt):
    global maxx
    if cnt==4:
        maxx = max(maxx,summ)
        return
    
    visited[i][j] = True
    summ+=paper[i][j]
    
    for u in range(4):
        y = i+dy[u]
        x = j+dx[u]
        if ((0<=y<n) & (0<=x<m)):
            if visited[y][x] == False:
                dfs(y,x,summ,cnt+1)
    

for i in range(n):
    paper.append(list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(m):
        visited = [[False] * m for _ in range(n)]
        dfs(i,j,0,0)
        print(maxx)
print(maxx)