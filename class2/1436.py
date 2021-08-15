a = int(input().strip())
count = 0
num = 666
three_six = '666'
while True:
    if three_six in str(num):
        count+=1
    if count==a:
        print(num)
        break
    num+=1
   