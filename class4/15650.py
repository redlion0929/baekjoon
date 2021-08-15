import sys
import itertools

n,m = map(int,sys.stdin.readline().rstrip().split())

for l in itertools.combinations(range(1,n+1),m):
    for k in l:
        print(k,end = " ")
    print()