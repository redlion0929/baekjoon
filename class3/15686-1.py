import sys
import itertools

n, m = map(int,sys.stdin.readline().rstrip().split())
mapp = []
chicken = []
house = []
    
for i in range(n):
    mapp.append([])
    line = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(len(line)):
        mapp[i].append(line[j])
        
        if line[j]==1:
            house.append([i,j])
        elif line[j] == 2:
            chicken.append([i,j])

summ = sys.maxsize

for i in itertools.combinations(chicken, m):
    min_sum= 0
    for j in house:
        minn = sys.maxsize
        for k in i:
            minn = min(minn, abs(j[0]-k[0])+abs(j[1]-k[1]))
        min_sum+=minn
    
    summ = min(summ,min_sum)
    
print(summ)