import sys
from collections import deque


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    line = sys.stdin.readline().rstrip()
    r_cnt = 0
    arr = deque()
    n = int(sys.stdin.readline().rstrip())
    arr_line = sys.stdin.readline().rstrip()
    error = False
    if n>0:
        for i in arr_line[1:-1].split(','):
            arr.append(int(i))
    
    for i in line:
        if i=="D":
            if len(arr)>0:
                if (r_cnt%2==1):
                    arr.pop()
                else:
                    arr.popleft()
            else:
                error = True
        else:
            r_cnt+=1
            
    if (r_cnt%2==1):
        arr = list(arr)[ : :-1]
        
    if error == True:
        print("error")
    else:
        print('[', end = "")
        for i in range(len(arr)):
            if i==len(arr)-1:
                print(arr[i],end = "")
            else:
                print(arr[i], end = ",")
        print(']')
        