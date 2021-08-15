import sys
n = int(input())
a = list(map(int,sys.stdin.readline().strip().split()))
a.sort()
m = int(input())
b = list(map(int,sys.stdin.readline().strip().split()))
r = []
for i in b:
    start, end = 0, n-1
    cnt = False
    while start<=end:
        mid = (start+end)//2
        if a[mid] == i:
            r.append(1)
            cnt = True
            break
        elif a[mid]<i:
            start = mid+1
        else:
            end = mid-1
    if cnt == False:
        r.append(0)
        
for i in r:
    print(i)