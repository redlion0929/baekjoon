import sys
n = int(sys.stdin.readline().strip())

result = [0 for _ in range(10001)]
for _ in range(n):
    result[int(sys.stdin.readline().strip())]+=1
for i in range(1,10001):
    if result[i]==0:
        continue
    else:
        for _ in range(result[i]):
            print(i)