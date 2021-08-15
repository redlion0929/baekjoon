import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

stack = deque()

def push(x):
    stack.append(x)
    
def size():
    return len(stack)
    
def empty():
    if size()==0:
        return 1
    else:
        return 0
    
def top():
    if empty()==1:
        return -1
    else:
        return stack[-1]
    
def pop():
    if empty()==1:
        return -1
    else:
        return stack.pop()
    
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    if line.split()[0] == "push":
        push(line.split()[1])
    
    elif line == "size":
        print(size())
    
    elif line == "empty":
        print(empty())
    
    elif line == "top":
        print(top())
      
    elif line == "pop":
        print(pop())
     
    else:
        exit()