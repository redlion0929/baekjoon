import sys
n, m = map(int, sys.stdin.readline().strip().split())
l = sorted(list(map(int, sys.stdin.readline().strip().split())))

s = sum(l)-m
i = 0
h = 0

while True:
    if i==0:
        if s>n*l[i]:
            s-=(n*l[i])
            h+=l[i]
            i+=1
            n-=1
        else:
            k = (s//n)
            h+=k
            break
    else:
        if s>n*(l[i]-l[i-1]):
            s-=(n*(l[i]-l[i-1]))
            h+=(l[i]-l[i-1])
            i+=1
            n-=1
        else:
            k = (s//n)
            h+=k
            break
print(h)