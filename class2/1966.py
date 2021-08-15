import sys
a = int(sys.stdin.readline().strip())
result = []
for _ in range(a):
    n, m = map(int, sys.stdin.readline().strip().split())
    q = list(map(int,sys.stdin.readline().strip().split()))
    idx = list(range(n))
    idx[m] = 'target'
    cnt = 0
    while len(q)>0:
        if q[0]==max(q):
            cnt+=1
            if idx[0]=='target':
                result.append(cnt)
                break
            else:
                del idx[0]
                del q[0]
        else:
            q.append(q[0])
            del q[0]
            idx.append(idx[0])
            del idx[0]
for i in result:
    print(i)      