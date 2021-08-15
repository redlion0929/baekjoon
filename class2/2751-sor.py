import sys
n = int(sys.stdin.readline().strip())
l = [int(sys.stdin.readline().strip()) for _ in range(n)]
for i in sorted(l):
    print(i)