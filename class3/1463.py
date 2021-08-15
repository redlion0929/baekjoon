import sys

n = int(sys.stdin.readline().rstrip())

result = [0,0,1,1]

for i in range(4, n+1):
    if i%3==0:
        if i%2==0:
            result.append(min(result[i//3], result[i//2], result[i-1])+1)
        else:
            result.append(min(result[i//3], result[i-1])+1)
            
    else:
        if i%2==0:
            result.append(min(result[i//2], result[i-1])+1)
        else:
            result.append(result[i-1]+1)
print(result[n])