import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
dx_l = [-1,0,-1,0]
dy_l = [-1,-1,0,0]
q =deque()

blue = []
white = []

def search():
    while q:
        i,j,cnt = q.popleft()
        time = n//cnt
        for u in range(4):
            y_l = i+ time *dy_l[u]
            x_l = j+time * dx_l[u]
            y_s = y_l-time
            x_s = x_l-time
            col = paper[y_s][x_s]
            is_fin = True
            for a in range(y_s,y_l):
                for b in range(x_s,x_l):
                    if paper[a][b]!=col:
                        is_fin = False
                        break
                if is_fin == False:
                    break
                    
            if is_fin == False:
                q.append([y_l,x_l,cnt*2])
            else:
                if col==0:
                    white.append(True)
                else:
                    blue.append(True)



paper = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

a = paper[0][0]
is_one = True

for i in range(len(paper)):
    for j in range(len(paper[i])):
        if paper[i][j]!=a:
            is_one = False
            break
if is_one:
    if a==0:
        print(1)
        print(0)
        exit()
    else:
        print(0)
        print(1)
        exit()

q.append([n,n,2])        
search()

print(len(white))
print(len(blue))