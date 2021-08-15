import sys
a = []
while True:
    s = sys.stdin.readline().strip()
    if int(s) == 0:
        break
    else:
        b = s[::-1]
        if b==s:
            a.append("yes")
        else:
            a.append("no")
for i in a:
    print(i)