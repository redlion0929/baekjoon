import sys
n = int(sys.stdin.readline().strip())
b5 = n//5
b3 = (n-b5*5)//3

while True:
    if (b5*5 + b3*3 ==n): 
        print(b5+b3)
        exit()
    else:
        b5-=1
        b3 = (n-b5*5)//3
        
    if b5==-1:
        print(-1)
        exit()