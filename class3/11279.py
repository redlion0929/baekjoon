import sys
import heapq
n = int(sys.stdin.readline().rstrip())
max_heap = []
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x==0:
        if len(max_heap)!=0:
            print(heapq.heappop(max_heap)[1])
        else:
            print(0)
    elif x>0:
        heapq.heappush(max_heap,(-x,x))
    else:
        exit()