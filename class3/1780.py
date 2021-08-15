import sys
n = int(sys.stdin.readline().rstrip())

paper0 = 0
paper1 = 0
paper2 = 0

def search(y,x,n):
    global paper0, paper1, paper2
    col = paper[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if col!=paper[i][j]:
                for a in range(3):
                    for b in range(3):
                        search(y+a*n//3,x+b*n//3,n//3)
                        return
    if col==-1:
        paper0+=1
        return
    elif col==0:
        paper1+=1
        return
    else:
        paper2+=1
        return

paper = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

search(0,0,n)
print(paper0)
print(paper1)
print(paper2)