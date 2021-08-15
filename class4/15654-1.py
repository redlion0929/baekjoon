import sys
n,m = map(int,sys.stdin.readline().rstrip().split())

check = [False]* n
result = [0]*m

l = sorted(list(map(int,sys.stdin.readline().rstrip().split())))

def backtracking(idx,m):
    if idx == m:
        for i in result:
            print(i, end = " ")
        print()
        return
    
    for i in range(n):
        if check[i]==False:
            result[idx] = l[i]
            check[i] = True
            backtracking(idx+1,m)
            check[i] = False
            
backtracking(0,m)