import sys
n = int(sys.stdin.readline().strip())
coord = []

for _ in range(n):
    coord.append(list(map(int,sys.stdin.readline().strip().split())))

for i in sorted(coord, key = lambda x: (x[0], x[1])):
    print(i[0],i[1])