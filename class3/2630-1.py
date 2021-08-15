import sys

n = int(sys.stdin.readline().rstrip())

paper = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

white = 0
blue = 0

def search(y,x,n):
    global white,blue
    col = paper[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if col!=paper[i][j]:
                search(y,x,n//2)
                search(y,x+n//2,n//2)
                search(y+n//2,x,n//2)
                search(y+n//2,x+n//2,n//2)
                return
                
    if col == 0:
        white+=1
        return
    else:
        blue+=1
        return
    
search(0,0,n)
print(white)
print(blue)