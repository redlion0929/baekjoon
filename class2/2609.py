import sys
a, b = map(int, sys.stdin.readline().strip().split())

if a<b:
    a, b = b, a

def gcd(a, b):
    if b==0:
        return a
    r = a%b
    return gcd(b, r)

print(gcd(a,b))
print(a*b//gcd(a,b))