import sys
n, m = map(int,sys.stdin.readline().rstrip().split())
check = [0] * (n+1)
result = [0] * m

def backtracking(idx, m):
    if idx==m:
        for i in result:
            print(i, end = " ")
        print()
        return
    
    for i in range(1,n+1):
        if check[i]==1:
            continue
        result[idx] = i
        
        for j in range(i+1):
            check[j] = 1
            
        backtracking(idx+1,m)
        
        for j in range(n+1):
            check[j] = 0
            
backtracking(0,m)