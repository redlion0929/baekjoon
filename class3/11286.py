import sys
import heapq

n = int(sys.stdin.readline().rstrip())
abs_heap = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x!=0:
        heapq.heappush(abs_heap, (abs(x), x))
    else:
        if len(abs_heap)==0:
            print(0)
        else:
            print(heapq.heappop(abs_heap)[1])
        