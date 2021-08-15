import sys
n = int(sys.stdin.readline().rstrip())
l = list(map(int, sys.stdin.readline().rstrip().split()))
sec = [1]*len(l)

for i in range(len(l)):
    for j in range(i):
        if l[i]>l[j]:
            sec[i] = max(sec[i],sec[j]+1)
print(max(sec))