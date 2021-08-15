import sys
from collections import deque
sys.setrecursionlimit(10000)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(sys.stdin.readline().rstrip())
grid = []
check_o = [[False] *n for _ in range(n)]
check_x = [[False] *n for _ in range(n)]

cnt_o = 0
cnt_x = 0

def dfs_o(R,i,j):
    check_o[i][j] = R
    for u in range(4):
        y = i +dy[u]
        x = j +dx[u]
        if ((0<=y<n) & (0<=x<n)):
            if check_o[y][x] == False:
                if R == "B":
                    if grid[y][x] == "B":
                        dfs_o(R,y,x)
                else:
                    if ((grid[y][x] == "R") | (grid[y][x] == "G")):
                        dfs_o(R,y,x)
                        
def dfs_x(R,i,j):
    check_x[i][j] = R
    for u in range(4):
        y = i +dy[u]
        x = j +dx[u]
        if ((0<=y<n) & (0<=x<n)):
            if ((grid[y][x] == R) & (check_x[y][x] == False)):
                dfs_x(R,y,x)

for i in range(n):
    grid.append([])
    line = sys.stdin.readline().rstrip()
    for j in line:
        grid[i].append(j)


for i in range(n):
    for j in range(n):
        if check_o[i][j] == False:
            cnt_o+=1
            dfs_o(grid[i][j],i,j)
        if check_x[i][j] == False:
            cnt_x+=1
            dfs_x(grid[i][j],i,j)
            
print(cnt_x, cnt_o)