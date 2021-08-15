import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

dict = {}

for _ in range(n):
    site, password = sys.stdin.readline().rstrip().split()
    dict[site] = password
for _ in range(m):
    line = sys.stdin.readline().rstrip()
    print(dict[line])