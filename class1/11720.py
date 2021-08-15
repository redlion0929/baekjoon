a = int(input().strip())
s = input().strip()
sum = 0
if len(s)==a:
    for i in s:
        sum+=int(i)
    
print(sum)