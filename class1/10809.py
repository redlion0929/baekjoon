s = input().strip()
a = [ -1 for i in range(ord('a'),ord('z')+1)]
for i,j in enumerate(s):
    idx = ord(j)-ord('a')
    if a[idx] == -1:
        a[idx] = i 
    else:
        pass
for i in a:
    print(i, end = " ")
