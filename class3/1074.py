import sys
n, r, c = map(int,sys.stdin.readline().rstrip().split())
cnt = 0

while n>1:
    ro = r//(2**(n-1))
    co = c//(2**(n-1))
    num = (2**(2*n-1))*ro+(2**(2*n-2))*co
    cnt+=num
    r = r-(ro * (2**(n-1)))
    c = c-(co*(2**(n-1)))
    n = n-1
    
if n==1:
    cnt+=(2*r+c)
        
print(cnt)