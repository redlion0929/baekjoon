import sys
n = int(sys.stdin.readline().rstrip())
tri = []

for _ in range(n):
    l = list(map(int,sys.stdin.readline().rstrip().split()))
    tri.append(l)
    
for i in range(1,len(tri)):
    for j in range(len(tri[i])):
        if i==1:
            tri[i][j] = tri[i-1][0]+tri[i][j]
        elif j==0:
            tri[i][j] = tri[i-1][j]+tri[i][j]
        elif j==i:
            tri[i][j] = tri[i-1][j-1]+tri[i][j]
        else:
            tri[i][j] = max(tri[i-1][j], tri[i-1][j-1])+tri[i][j]

print(max(tri[n-1]))