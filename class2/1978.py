import sys

def sosu(m):
    if m==1:
        return False
    for i in range(2,int(m**0.5)+1):
        if (m%i==0):
            return False
    return True

n = int(sys.stdin.readline().strip())
s = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0
for i in s:
    if sosu(i):
        cnt+=1
print(cnt)