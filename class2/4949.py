import sys
from collections import deque

while True:
    balanced = True
    line = sys.stdin.readline().rstrip()
    if line==".":
        exit()
    stack = deque()
    i = 0
    while line[i]!=".":
        if ((line[i]=="(") | (line[i]=="[")):
            stack.append(line[i])
        elif ((line[i]==")") | (line[i]=="]")):
            if len(stack)==0:
                balanced = False
                break
            if line[i]==")":
                if (stack.pop()!="("):
                    balanced = False
                    break
            else:
                if (stack.pop()!="["):
                    balanced = False
                    break
        i+=1
        
    if ((balanced) & (len(stack)==0)):
        print("yes")
    else:
        print("no")
        
        //if stack : 이 구문은 stack이 비었으면 false이다.