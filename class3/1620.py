import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

dogam_name = {}
dogam_num = []

for i in range(n):
    line = sys.stdin.readline().rstrip()
    dogam_name[line] =  i
    dogam_num.append(line)

for i in range(m):
    q =sys.stdin.readline().rstrip()
    try:
        num = int(q)
        print(dogam_num[num-1])
    except:
        print(dogam_name[q]+1)
    