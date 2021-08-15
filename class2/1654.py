import sys
a, b = map(int, sys.stdin.readline().strip().split())
l = [int(sys.stdin.readline().strip()) for i in range(a)]
start, end = 1, max(l)
while start<=end:
    mid = (start+end)//2
    cnt=0
    for i in l:
        cnt+=(i//mid)
    if cnt<b:
        end = mid-1
    else:
        start = mid+1
print(end)