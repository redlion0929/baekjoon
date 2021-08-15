import sys
from collections import deque
n = int(sys.stdin.readline().strip())
q = deque(list(range(1,n+1)))
for i in range(n-1):
    q.popleft()
    q.append(q.popleft())
print(q[0])