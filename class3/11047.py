import sys
n,k = map(int,sys.stdin.readline().rstrip().split())
coin = []
result = 0

for _ in range(n):
    money = int(sys.stdin.readline().rstrip())
    if money<k:
        coin.append(money)
        
for i in range(len(coin)):
    if k==0:
        break
    m = k//coin[len(coin)-1-i]
    result+=m
    k-=m*coin[len(coin)-1-i]

print(result)