import sys
n = int(sys.stdin.readline().strip())

for i in range(1, n) :
    s = str(i)
    t = 0
    for j in s:
        t+=int(j)
    if ((t+i) == n):
        print(i)
        exit()
print(0)