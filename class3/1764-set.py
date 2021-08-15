import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

not_listen = set()
not_see = set()
for _ in range(n):
    not_listen.add(sys.stdin.readline().rstrip())
for _ in range(m):
    not_see.add(sys.stdin.readline().rstrip())
    
kyo = not_listen & not_see
print(len(kyo))
for i in sorted(list(kyo)):
    print(i)