import sys
n = int(sys.stdin.readline().strip())

l = []
result = []
for i in range(n):
    wh = list(map(int,sys.stdin.readline().strip().split()))
    l.append(wh)
    
for i in range(len(l)):
    rank = 1
    for j in range(len(l)):
        if ((l[i][0]<l[j][0]) & (l[i][1]<l[j][1])):
            rank+=1
    result.append(rank)
    
for i in result:
    print(i, end = " ")
    
//문제를 풀 때 서로 같은 수가 있을 경우를 고민했었는데 그 경우 애초에 등수조차 정할 수 없다.