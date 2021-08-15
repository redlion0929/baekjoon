import sys
n = int(sys.stdin.readline().rstrip())
l = list(map(int,sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
v = list(map(int,sys.stdin.readline().rstrip().split()))

card = [0] * (max(l)-min(l)+1)

a = min(l)
b = max(l)

for i in l:
    card[i-a]+=1

for j in v:
    if ((j>=a)&(j<=b)):
        print(card[j-a],end = " ")
    else:
        print(0, end = " ")