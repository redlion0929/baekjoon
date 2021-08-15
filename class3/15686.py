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

result = [ [0]*len(house) for _ in range(len(chicken))]

for i in range(len(result)):
    for j in range(len(result[i])):
        result[i][j] = abs(chicken[i][0]-house[j][0])+abs(chicken[i][1]-house[j][1])

select = list(itertools.combinations(range(len(chicken)), m))
summ = sys.maxsize

for i in select:
    min_sum= 0
    for j in range(len(house)):
        minn = result[i[0]][j]
        for k in i:
            minn = min(minn, result[k][j])
        min_sum+=minn
    
    summ = min(summ,min_sum)
    
print(summ)

https://medium.com/@hckcksrl/python-permutation-combination-a7bf9e5d6ab3