import sys

result = []

while True:
    l = list(map(int, sys.stdin.readline().strip().split()))
    if (l[0]==l[1]==l[2]==0):
        break;
    l.sort()
    if (l[2]**2 == l[0]**2 + l[1]**2):
        result.append('right')
    else:
        result.append('wrong')
for i in result:
    print(i)