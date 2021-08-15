import sys
sys.setrecursionlimit(10000)
n,m = map(int,sys.stdin.readline().rstrip().split())

def c(n,m):
    if m==0:
        return 1
    if n==m:
        return 1
    else:
        return c(n-1,m)+c(n-1,m-1)
    
print(c(n,m))