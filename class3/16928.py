import sys
from collections import deque

visited =[0]*101
n, m = map(int, sys.stdin.readline().rstrip().split())
dice = {}
snake = {}

for _ in range(n):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    if x>=y:
        break
    dice[x] = y
    
    
for _ in range(m):
    u,v = map(int,sys.stdin.readline().rstrip().split())
    if u<=v:
        break
    snake[u] = v

def BFS(s,cnt):
    q = deque([(s,cnt)])
    visited[s] = 1
    while q:
        v,c = q.popleft()
        for i in range(1,7):
            next_val = v+i
            
            if next_val==100:
                print(c+1)
                return
            
            elif next_val<100:
                if next_val in dice:
                    next_val = dice[next_val]
                elif next_val in snake:
                    next_val = snake[next_val]
                    
                if visited[next_val] == 0:
                    q.append((next_val,c+1))
                    visited[next_val] = 1
                    
BFS(1,0)
