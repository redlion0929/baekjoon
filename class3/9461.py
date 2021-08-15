import sys
T = int(sys.stdin.readline().rstrip())
result = [0, 1, 1, 1, 2, 2]

r = [int(sys.stdin.readline().rstrip()) for _ in range(T)]
for i in range(6,max(r)+1):
    result.append(result[i-1]+result[i-5])
    
for i in r:
    print(result[i])