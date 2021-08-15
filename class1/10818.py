a = int(input().strip())
b= (input().strip()).split()
l = [int(i) for i in b]
if a!=len(l):
    exit()
print(min(l))
print(max(l))
    