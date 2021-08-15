import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

l = {}
result = []

for _ in range(n):
    line = sys.stdin.readline().rstrip()
    l[line] = 1
    
for _ in range(m):
    line = sys.stdin.readline().rstrip()
    try:
        if l[line]==1:
            result.append(line)
    except:
        continue
        
print(len(result))
for i in sorted(result):
    print(i)