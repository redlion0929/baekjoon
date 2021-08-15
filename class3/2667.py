import sys

n = int(sys.stdin.readline().rstrip())
map = []
check = [[False]*n for _ in range(n)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
result = []
cnt = 0 

def search(map, i, j):
    result[cnt]+=1
    map[i][j] = 1
    check[i][j] = True
    for u in range(4):
        if ((i+dy[u]>=0) & (i+dy[u]<=n-1) & (j+dx[u]>=0) & (j+dx[u]<=n-1)):
            if ((map[i+dy[u]][j+dx[u]]==1) & (check[i+dy[u]][j+dx[u]]==False)):
                check[i+dy[u]][j+dx[u]] = True
                search(map, i+dy[u], j+dx[u])
                
                
for i in range(n):
    map.append([])
    line = sys.stdin.readline().rstrip()
    for j in line:
        map[i].append(int(j))
        
for i in range(len(map)):
    for j in range(len(map[i])):
        if ((map[i][j] == 1) & (check[i][j] == False)):
            result.append(0)
            search(map,i,j)
            cnt+=1
            
print(cnt)
for i in sorted(result):
    print(i)