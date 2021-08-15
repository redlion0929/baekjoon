import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()
p = 'I'
for _ in range(n):
    p+='OI'

idx = 0
cnt = 0
try:
    idx =s.index(p,idx)+len(p)
    cnt+=1
    while True:
        if idx<=len(s)-2:
            if ((s[idx]=="O") & (s[idx+1] =="I")):
                cnt+=1
                idx+=2
            else:
                idx =s.index(p,idx)+len(p)
                cnt+=1
        else:
             print(cnt)
             break
except:
    print(cnt)
        
