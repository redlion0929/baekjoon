import sys
t = int(sys.stdin.readline().rstrip())

def dfs(start):
    visit[start] = True
    for i in range(n+2):
        if adj[start][i] == 1 and visit[i] == False:
            dfs(i)

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    node = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n + 2)]
    adj = [ [0] * (n+2) for _ in range(n+2)]
    visit = [False]*(n+2)
    for i in range(n+2):
        for j in range(n+2):
            if i==j:
                continue
            if abs(node[i][0]-node[j][0])+abs(node[i][1]-node[j][1])<=1000:
                adj[i][j] = 1
                adj[j][i] = 1
    dfs(0)
    if visit[n+1] == True:
        print("happy")
    else:
        print("sad")