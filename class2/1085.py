import sys
x, y, w, h = map(int, sys.stdin.readline().split())
if ((x>w) | (y>h)):
    exit()
s = [x, y, h-y, w-x]
print(min(s))