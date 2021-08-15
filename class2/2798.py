import sys
n, m = map(int,sys.stdin.readline().strip().split())
l = list(map(int,sys.stdin.readline().strip().split()))
l.sort()
max = 0
for i in range(len(l)-1, -1, -1):
    for j in range(i-1,-1,-1):
        for k in range(j-1,-1,-1):
            sum = l[i]+l[j]+l[k]
            if sum<=m:
                if sum>max:
                    max = sum
                    break;
print(max)