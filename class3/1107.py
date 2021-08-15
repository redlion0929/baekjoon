import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
btn = [True]*10
for i in list(map(int,sys.stdin.readline().rstrip().split())):
    btn[i] = False

min_cnt = abs(100-n)

for i in range(1000001):
    st = str(i)
    for j in range(len(st)):
        if btn[int(st[j])] == False:
            break
        if j == len(st)-1 :
            min_cnt = min(min_cnt, len(st)+ abs(n-i))
            
print(min_cnt)