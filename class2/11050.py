import sys

def factorial(a):
    if (a==1) | (a==0):
        return 1
    else:
        return a*factorial(a-1)

n, k = map(int, sys.stdin.readline().strip().split())

result = factorial(n)/(factorial(n-k)*factorial(k))
print(int(result))