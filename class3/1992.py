import sys
n = int(sys.stdin.readline().rstrip())
result = []
result_str = []

def search(y,x,n):
    col = tree[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if col!=tree[i][j]:
                result.append('(')
                search(y,x,n//2)
                search(y,x+n//2,n//2)
                search(y+n//2,x,n//2)
                search(y+n//2,x+n//2,n//2)
                result.append(')')
                return
    result.append(str(col))
    return


def arrange(result,i):
    if i==0:
        if len(result[i])==0:
            result_str.append([])
        else:
            result_str.append(result[i])
            return
    else:
        if len(result[i])==0:
            result_str[-1].append([])
            
    
            

tree = []
for i in range(n):
    line = sys.stdin.readline().rstrip()
    tree.append([])
    for j in line:
        tree[i].append(int(j))

search(0,0,n)
for i in result:
    print(i,end="")