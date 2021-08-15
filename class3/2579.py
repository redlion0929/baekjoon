import sys
n = int(sys.stdin.readline().rstrip())

stair = [0]
for _ in range(n):
    stair.append(int(sys.stdin.readline().rstrip()))
result = []

for i in range(n+1):
    if ((i==0) | (i==1)):
        result.append(stair[i])
    elif i==2:
        result.append(stair[i]+stair[i-1])
    else:
        result.append(max(result[i-3]+stair[i-1]+stair[i], result[i-2]+stair[i]))
        
print(result[n])