import sys

from collections import Counter

n, m, b = map(int, sys.stdin.readline().rstrip().split())
ground = []

for _ in range(n):
    line = sys.stdin.readline().rstrip().split()
    for i in line:
        ground.append(int(i))

min_sec = 1000000000
h = 0

gr = Counter(ground)

for i in range(257):
    sec = 0
    item = b
    for j in gr:
        if j>i:
            sec+=((2*(j-i))*gr[j])
            item+=((j-i) * gr[j])
        else:
            sec+=((i-j)*gr[j])
            item-=((i-j)*gr[j])
    
    if item>=0:
        if min_sec>=sec:
            min_sec = sec
            h = i
        
print(min_sec, h)