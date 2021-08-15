import sys
n = int(sys.stdin.readline().rstrip())
            
num = int(n ** 0.5)
mini = 4

for i in range(num,int((n//4)**0.5)-1,-1):
    if i**2 == n:
        mini = 1
        break
    else:
        t = n-(i**2)
        for j in range(int(t**0.5), int((t//3)**0.5)-1,-1):
            if i**2 + j**2 == n:
                mini = 2
                break
            else:
                u = n-(i**2+j**2)
                for k in range(int(u**0.5), int((u//2)**0.5)-1,-1):
                    if i**2+j**2+k**2 == n:
                        mini = min(3, mini) 
                        continue
print(mini)