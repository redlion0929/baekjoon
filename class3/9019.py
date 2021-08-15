import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

def D(n):
    return (2*n)%10000

def S(n):
    return (n-1)%10000

def L(n):
    return (n%1000)*10+n//1000
    
def R(n):
    return (n%10)*1000+n//10
        

def bfs(B):
    while q:
        n, cnt = q.popleft()
        
        d = D(n)
        if d == B:
            return cnt+"D"
        elif num[d] == 0:
            num[d] =1
            q.append([d,cnt+"D"])
                        
        s = S(n)
        if s == B:
            return cnt+"S"
        elif num[s] == 0:
            num[s] =1
            q.append([s,cnt+"S"])
                
        l = L(n)
        if l == B:
            return cnt+"L"
        elif num[l] == 0:
            num[l] =1
            q.append([l,cnt+"L"])
                
        r = R(n)         
        if r == B:
            return cnt+"R"
        elif num[r] == 0:
            num[r] =1
            q.append([r,cnt+"R"])
    
    
for _ in range(T):
    A, B = map(int,sys.stdin.readline().rstrip().split())
    num = [0]*10000
    q = deque()
    q.append([A,""])
    print(bfs(B))