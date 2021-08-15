import sys

INF = sys.maxsize

n = int(sys.stdin.readline().rstrip())
result = []

for i in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    result.append([])
    for j in line:
        result[i].append(j)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if ((result[i][k] == 1) & (result[k][j] == 1)):
                result[i][j] = 1
                
for i in result:
    for j in i:
        print(j, end = " ")
    print()