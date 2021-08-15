import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
l = sorted(list(set(map(int,sys.stdin.readline().rstrip().split()))))

check = [False] * len(l)
result = [0]*m

def backtracking(idx,m):
    if idx == m:
        for i in result:
            print(i, end = " ")
        print()
        return
    
    for i in range(len(l)):
        if check[i] == False:
            result[idx] = l[i]
            for j in range(i):
                check[j] = True
                
            backtracking(idx+1,m)
            
            for j in range(len(l)):
                check[j] = False
            
backtracking(0,m)