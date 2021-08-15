import sys
n, k = map(int, sys.stdin.readline().rstrip().split())

result = []
l = list(range(1, n+1))
i = 0

for _ in range(n):
    idx = (i+k-1)%len(l)
    result.append(l.pop(idx))
    i = idx
    
print("<", end = "")

for j in range(len(result)):
    if (j==len(result)-1):
        print(result[j],end = ">")
    else:
        print(result[j], end = ", ")
        
    