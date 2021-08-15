import sys
n,m = map(int,sys.stdin.readline().rstrip().split())
l = list(map(int,sys.stdin.readline().rstrip().split()))
s = [0]*(len(l)+1)

for i in range(1,len(l)+1):
    s[i] = s[i-1]+l[i-1]
    
for _ in range(m):
    i,j = map(int,sys.stdin.readline().rstrip().split())
    print(s[j]-s[i-1])