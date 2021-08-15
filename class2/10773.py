import sys
n = int(sys.stdin.readline().strip())
result = []

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num==0:
        if len(result)==0:
            continue
        else:
            del result[-1]
    else:
        result.append(num)
print(sum(result))