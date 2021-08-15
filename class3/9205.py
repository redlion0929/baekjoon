import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
INF = sys.maxsize

for _ in range(t):
    graph = []
    n = int(sys.stdin.readline().rstrip())
    home_x, home_y = map(int,sys.stdin.readline().rstrip().split())
    graph.append([home_x,home_y])
    for _ in range(n):
        con_x, con_y = map(int,sys.stdin.readline().rstrip().split())
        graph.append([con_x,con_y])
    end_x, end_y = map(int,sys.stdin.readline().rstrip().split())
    graph.append([end_x,end_y])
    
    adj_mat = []
    
    for i in range(len(graph)):
        adj_mat.append([])
        for j in range(len(graph)):
            dist = abs(graph[i][0]-graph[j][0])+abs(graph[i][1]-graph[j][1])
            if dist<=1000:
                adj_mat[i].append(dist)
            else:
                adj_mat[i].append(INF)
    
    
    for k in range(len(graph)):
        for i in range(len(adj_mat)):
            for j in range(len(adj_mat[i])):
                adj_mat[i][j] = min(adj_mat[i][j], adj_mat[i][k]+adj_mat[k][j])
    
    if adj_mat[0][-1] == INF:
        print("sad")
    else:
        print("happy")