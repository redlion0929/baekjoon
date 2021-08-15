import sys
n = int(input().strip())
a=[]
for i in range(n):
    s = sys.stdin.readline().strip()
    if s not in a:
        a.append(s)
a.sort(key = lambda x: (len(x),x))
for i in a:
    print(i)