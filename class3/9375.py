import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    result = 1
    dict = {}
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        a, b = sys.stdin.readline().rstrip().split()
        if b in dict:
            dict[b].append(a)
        else:
            dict[b] = []
            dict[b].append(a)
           
    for i in dict:
        result*=(len(dict[i])+1)
        
    print(result-1)
