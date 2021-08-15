import sys
from collections import deque

n = int(sys.stdin.readline().strip())

for _ in range(n):
    balanced = True
    line = sys.stdin.readline().rstrip()
    stack = deque()
    for i in line:
        if (i=="("):
            stack.append(i)
        elif (i==")"):
            if stack and (stack[-1] == "("):
                stack.pop()
            else:
                balanced = False
                break
    if ((balanced) & (len(stack)==0)):
        print("YES")
    else:
        print("NO")
        
        