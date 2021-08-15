import sys

T = int(sys.stdin.readline().strip())
result = []
for _ in range(T) :
    H, W, N = map(int, sys.stdin.readline().strip().split())
    m = N%H
    v = N//H
    if m==0:
        Y = H
        X = v
    else:
        Y = m
        X = v+1
        
    Y = str(Y)
    if X<10:
        X = '0'+str(X)
    else:
        X = str(X)
    
    result.append(int(Y+X))
    
for i in result:
    print(i)