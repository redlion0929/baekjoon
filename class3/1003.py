import sys
T = int(sys.stdin.readline().rstrip())

zero = [1, 0]
one = [0, 1]

test = []


for _ in range(T):
    num = int(sys.stdin.readline().rstrip())
    test.append(num)
    

for i in range(2, max(test)+1):
    zero.append(zero[i-1]+zero[i-2])
    one.append(one[i-1]+one[i-2])
    
for i in test:
    print(zero[i], one[i])