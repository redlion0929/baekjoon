import sys
n = int(input())
a = list(map(int,sys.stdin.readline().strip().split()))
a.sort()
m = int(input())
b = list(map(int,sys.stdin.readline().strip().split()))

def binary_search(a, v, start, end):
    if start>end:
        return 0
    mid = (start+end)//2
    if a[mid]==v:
        return 1
    elif a[mid]>v:
        return binary_search(a,v,start, mid-1)
    else:
        return binary_search(a,v,mid+1, end)
for i in b:
    start, end = 0, n-1
    print(binary_search(a, i, start, end))