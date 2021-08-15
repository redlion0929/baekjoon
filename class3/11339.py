import sys
n = int(sys.stdin.readline().rstrip())
r = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
sum=0
for i in range(len(r)):
    for j in range(i+1):
        sum+=r[j]
        
print(sum)