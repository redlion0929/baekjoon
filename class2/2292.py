import sys
n = int(sys.stdin.readline().strip())

a =1
r = 1
room = 1
while True:
    if n<=a:
        print(room)
        break
    else:
        a+= (6*r)
        room+=1
        r+=1