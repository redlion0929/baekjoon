import sys
A, B, V = map(int, sys.stdin.readline().strip().split())

up_per_day = A-B
h = V-A
days = 0
if h%up_per_day==0:
    days = int(h/up_per_day)+1
else:
    days = int(h/up_per_day)+2

print(days)