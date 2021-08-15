a = input().upper()
b = [a.count(chr(i)) for i in range(ord('A'),ord('Z')+1)]

c = max(b)

if b.count(c) == 1 :
    print(chr(b.index(c)+ord('A')))
else:
    print('?')