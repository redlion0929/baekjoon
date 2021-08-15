import sys
n = int(sys.stdin.readline().strip())

rank = 0
per = 0
r = []
result = [0]*n

for i in range(n):
    wh = list(map(int,sys.stdin.readline().strip().split()))
    r.append(wh)
l = sorted(range(len(r)), key = lambda x : (-r[x][0],-r[x][1]))

for i,j in enumerate(l):
    if i==0:
        rank +=1
        per+=1
        result[j]=rank
        continue
    else:
        if r[l[i-1]][1]<=r[l[i]][1]:
            per+=1
            result[j] = rank
            continue
        else:
            rank=per+1
            per+=1
            result[j]=rank
            
for i in result:
    print(i, end=" ")
    
    //88 200
88 100
88 150
60 200
40 100 이 경우 1 3 2 3 5출력 문제가 생긴다. (2,3,4번째 원소들 사이의 순서 모호)