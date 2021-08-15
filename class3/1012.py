import sys
sys.setrecursionlimit(10000)
T = int(sys.stdin.readline().rstrip())

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def search(gr,i, j):
    for u in range(4):
        if ((i+dy[u]>=0) & (i+dy[u]<=n-1) & (j+dx[u]>=0) & (j+dx[u]<=m-1)):
            if ((gr[i+dy[u]][j+dx[u]]==1) & (check[i+dy[u]][j+dx[u]]==False)):
                gr[i+dy[u]][j+dx[u]]= -1
                check[i+dy[u]][j+dx[u]]=True
                search(gr, i+dy[u], j+dx[u])
        
        
for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    cnt = 0
    gr = [[0]*m for _ in range(n)]
    check = [[False]*m for _ in range(n)]
    
    for _ in range(k):
        j, i = map(int,sys.stdin.readline().rstrip().split())
        gr[i][j] = 1
    
    
    for i in range(len(gr)):
        for j in range(len(gr[i])):
            if ((gr[i][j]==1) & (check[i][j]==False)):
                cnt+=1
                search(gr,i,j)
            
    print(cnt)