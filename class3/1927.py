import sys
import heapq

n = int(sys.stdin.readline().rstrip())
min_heap = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x!=0:
        heapq.heappush(min_heap,x)
    else:
        if len(min_heap)==0:
            print(0)
        else:
            print(heapq.heappop(min_heap))
            