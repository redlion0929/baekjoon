import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
dy = [-1,1,0,0]
dx = [0,0,-1,1]

baby = [0,0]
fish = {}
space = []
baby_size = 2
sec = 0
cnt = 0

def find_food():
    while q:
        i,j = q.popleft()
        for u in range(4):
            y=i+dy[u]
            x=j+dx[u]
            if ((0<=y<n) & (0<=x<n)):
                if ((visited[y][x] == -1) & (space[y][x]<=baby_size)):
                    visited[y][x] = visited[i][j]+1
                    q.append([y,x])
    
for i in range(6):
    fish[i+1] = []

for i in range(n):
    space.append([])
    line = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(len(line)):
        space[i].append(line[j])
        if line[j] == 0:
            continue
        elif line[j]==9:
            baby = [i,j]
        else:
            fish[line[j]].append([i,j])
            
space[baby[0]][baby[1]] = 0

while True:
    visited = [[-1]*n for _ in range(n)]
    visited[baby[0]][baby[1]] = 0
    food = []
    q = deque()
    q.append(baby)
    find_food()
    
    if baby_size<=7:
        size = baby_size
    else:
        size = 7
        
    for i in range(1,size):
        for j in fish[i]:
            if ((space[j[0]][j[1]]!=0) & (visited[j[0]][j[1]]!=-1)):
                y,x, dist = j[0],j[1],visited[j[0]][j[1]]
                food.append([y,x,dist])
                
    if len(food)==0:
        print(sec)
        exit()
    else:
        food = sorted(food, key = lambda x: (x[2],x[0],x[1]))
        eat = food[0]
        sec+=eat[2]
        baby = [eat[0],eat[1]]
        space[eat[0]][eat[1]] = 0
        cnt+=1
        if cnt==baby_size:
            cnt = 0
            baby_size+=1
            
1. 먹이 크기 순이 아니라 거리순이야
2. 갈 수 있는 곳이 없다면 food에 넣으면 안돼
3. 코드 간소화
                 