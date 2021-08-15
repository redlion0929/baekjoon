import sys

n, m = map(int,sys.stdin.readline().rstrip().split())
l = sorted(list(map(int,sys.stdin.readline().rstrip().split())))

check = [False] * n
result = [0] * m

def backtracking(idx, m):
    if idx==m:
        for i in result:
            print(i,end = " ")
        print()
        return
    
    for i in range(n):
        if check[i] == False:
            result[idx] = l[i]
            for j in range(i):
                check[j] = True //마지막 줄에서 False로 초기화 시켜도 어처피 다시 실행될때 여기서 True로 막힌다.
            backtracking(idx+1,m)
            
            for j in range(n):
                check[j] = False
        
            
backtracking(0,m)