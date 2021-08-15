import sys
from collections import Counter

n = int(sys.stdin.readline().strip())
l = list([int(sys.stdin.readline().strip()) for _ in range(n)])

l.sort()
print(round(sum(l)/len(l)))

print(l[int(len(l)/2)])

cnt = Counter(l)
c = cnt.most_common()

if len(l)==1:
    print(l[0])
else:
    if c[0][1]!=c[1][1]:
        print(c[0][0])
    else:
        print(c[1][0])

print(max(l)-min(l))