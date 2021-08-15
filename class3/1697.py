import sys
from collections import deque

d1 = [1,1,2]
d2 = [1,-1,0]
n,k = map(int, sys.stdin.readline().rstrip().split())
visited = [False]*100001

def bfs():
    while q:
        x, cnt = q.popleft()
        if x == k:
            print(cnt)
            exit()
        for u in range(3):
            new_x = d1[u]*x+d2[u]
            if 0<=new_x<100001:
                if visited[new_x] == False:
                    visited[new_x] = True
                    q.append([new_x,cnt+1])
        
q = deque()
q.append([n,0])
visited[n] = True
bfs()