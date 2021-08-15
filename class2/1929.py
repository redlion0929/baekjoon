a, b = map(int,input().strip().split())
def is_sosu(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if (n%i==0):
            return False
    return True

for i in range(a,b+1):
    if is_sosu(i):
        print(i)