import sys
import itertools

n,m = map(int,sys.stdin.readline().rstrip().split())

l = sorted(list(map(int,sys.stdin.readline().rstrip().split())))

for i in sorted(list(set(itertools.permutations(l,m)))):
    for j in i:
        print(j,end = " ")
    print()
