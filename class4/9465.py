import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    st = []
    n = int(sys.stdin.readline().rstrip())
    for _ in range(2):
        line = list(map(int, sys.stdin.readline().rstrip().split()))
        st.append(line)
        
        max_ = 0
        for i in range(len(st)):
            for j in range(len(st[i])):
                ar = st
                max_ = max(max_,select(ar,i,j,cnt))
                
                
def select(ar, i, j, cnt, sum_):
    if cnt == 3 or ((i==len(ar)-1) and (j == len(ar[i])-1)):
        return sum_
    else:
        
        