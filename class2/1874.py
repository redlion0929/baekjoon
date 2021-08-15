import sys
a = int(sys.stdin.readline().strip())
s = [int(sys.stdin.readline().strip()) for _ in range(a)]
si = 0
n = 1
q = [0]
r=[]
while si<len(s):
    if s[si]==q[-1]:
        si+=1
        r.append('-')
        del q[-1]
    elif s[si]<q[-1]:
        print('NO')
        exit()
    else:
        if n<=a:
            while n<=s[si]:
                q.append(n)
                r.append('+')
                n+=1
for i in r:
    print(i)