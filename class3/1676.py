import sys

n = int(sys.stdin.readline().rstrip())

result = []
cnt = 0
for i in range(1,n+1):
    num = i
    while(num%5==0):
        num/=5
        cnt+=1

print(cnt)