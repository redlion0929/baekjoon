import sys
n = int(sys.stdin.readline().strip())

r = []

for i in range(n):
    line = sys.stdin.readline().strip().split()
    an = [int(line[0]), line[1]]
    r.append(an)
    
l = sorted(r, key = lambda x : (x[0], r.index(x)))

for i in l:
    print(i[0], i[1])
    
//위의 경우는 시간초과, 백준의코드가 정답 그냥 나이 순으로 정렬할 경우, 같은 값일경우 기존 배열의 인덱스 순에 따라 정렬된다.,