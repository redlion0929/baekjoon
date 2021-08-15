import sys
import heapq
t = int(sys.stdin.readline().rstrip())

def same(q):
    while q and total[q[0][1]] == False:
        heapq.heappop(q)
        
for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    min_q = []
    max_q = []
    total = []
    i = 0
    for _ in range(k):
        func, n = sys.stdin.readline().rstrip().split()
        n = int(n)
        if func=="I":
            heapq.heappush(min_q,(n,i))
            heapq.heappush(max_q,(-n,i))
            total.append(True)
            i+=1
        else:
            if n==1:
                same(max_q)
                if len(max_q)!=0:
                    total[heapq.heappop(max_q)[1]] = False
            else:
                same(min_q)
                if len(min_q)!=0:
                    total[heapq.heappop(min_q)[1]] = False
                    
    same(max_q)
    same(min_q)
    
    if True in total:
        print(-1*max_q[0][0], min_q[0][0])
    else:
        print("EMPTY")