import sys
n = int(sys.stdin.readline().rstrip())
conference = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    conference.append([s,e])
    
conference = sorted(conference, key = lambda x:x[0])
conference = sorted(conference, key = lambda x:x[1])
cnt = 0
end_time = 0
for i in conference:
    if end_time<=i[0]:
        cnt+=1
        end_time = i[1]
        
print(cnt)