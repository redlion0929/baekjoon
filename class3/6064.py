import sys
t = int(sys.stdin.readline().rstrip())

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
def lcm(a,b):
    return (a*b)//gcd(a,b)


for _ in range(t):
    m,n,x,y = map(int,sys.stdin.readline().rstrip().split())
    max1, min1= max(m,n), min(m,n)
    if max1 == m:
        max2 = x
        min2 = y
    else:
        max2 = y
        min2 = x
    lc = lcm(max1,min1)
    i = 0
    while True:
        year = i*max1+max2
        if year>lc:
            print(-1)
            break
        
        if (((year-min2)%min1)==0):
            print(year)
            break
        i+=1