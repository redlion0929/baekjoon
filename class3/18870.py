import sys
n = int(sys.stdin.readline().rstrip())
l = list(map(int,sys.stdin.readline().rstrip().split()))
result = {}
s = sorted(list(set(l)))
for i in range(len(s)):
    result[s[i]] = i
    
for i in range(len(l)):
    print(result[l[i]], end = " ")