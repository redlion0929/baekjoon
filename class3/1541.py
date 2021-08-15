import sys
line = sys.stdin.readline().rstrip()
line = line.split('-')
result = 0
for i in line[0].split('+'):
    result+=int(i)
for i in line[1:]:
    for j in i.split('+'):
        result-=int(j)
        
print(result)