a = (input().strip()).split()
n = int(a[0])
x = int(a[1])
s = (input().strip()).split()
s = [int(i) for i in s]
for i in s:
    if i<x:
        print(i, end=" ")
    