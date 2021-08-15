a = int(input().strip())
b =[]
for i in range(a):
    h = list(map(int, input().split()))
    b.append(h[0]+h[1])
for i in b:
    print(i)