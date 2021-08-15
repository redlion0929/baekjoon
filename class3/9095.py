import sys
T = int(sys.stdin.readline().rstrip())
l = [int(sys.stdin.readline().rstrip()) for _ in range(T)]
result = [0,1,2,4]

for i in range(4, max(l)+1):
    result.append(0)
    for k in range(1,4):
        result[i]+=(result[i-k])
        
for i in l:
    print(result[i])