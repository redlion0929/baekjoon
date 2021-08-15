import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

queue = deque()

def push(x):
    queue.append(x)
    
def size():
    return len(queue)
    
def empty():
    if size()==0:
        return 1
    else:
        return 0
    
def pop():
    if empty()==1:
        return -1
    else:
        return queue.popleft()

def front():
    if empty()==1:
        return -1
    else:
        return queue[0]

def back():
    if empty()==1:
        return -1
    else:
        return queue[-1]
    
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    if line.split()[0] == "push":
        push(line.split()[1])
    
    elif line == "size":
        print(size())
    
    elif line == "empty":
        print(empty())
    
    elif line == "front":
        print(front())
        
    elif line == "back":
        print(back())
      
    elif line == "pop":
        print(pop())
     
    else:
        exit()