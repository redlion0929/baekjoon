import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
deq = deque()

def empty():
    if len(deq)==0:
        return 1
    else:
        return 0
    
def pop_front():
    if empty()==1:
        print(-1)
    else:
        print(deq.popleft())
        
def pop_back():
    if empty()==1:
        print(-1)
    else:
        print(deq.pop())

        
def front():
    if empty()==1:
        print(-1)
    else:
        print(deq[0])
        
def back():
    if empty()==1:
        print(-1)
    else:
        print(deq[-1])
        
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    op = line.split()[0]
    if op =="push_front":
        deq.appendleft(line.split()[1])
        
    elif op == "push_back":
        deq.append(line.split()[1])
        
    elif op == "pop_front":
        pop_front()
    
    elif op == "pop_back":
        pop_back()
    
    elif op=="size":
        print(len(deq))
    
    elif op == "empty":
        print(empty())
        
    elif op == "front":
        front()
        
    elif op == "back":
        back()
        
    else:
        exit()