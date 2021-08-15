import sys
n, m = map(int, sys.stdin.readline().strip().split())
l = []
d = []
for i in range(n):
    l.append(sys.stdin.readline().strip())
    
for i in range(n-7):
    for j in range(m-7):
        count = 0
        for r in range(8):
            for c in range(8):
                if (r%2==0):
                    if (c%2==0):
                        if l[i+r][j+c]!='B':
                            count+=1
                        else:
                            count+=0
                    else:
                        if l[i+r][j+c]!='W':
                            count+=1
                        else:
                            count+=0
                else:
                    if (c%2==0):
                        if l[i+r][j+c]!='W':
                            count+=1
                        else:
                            count+=0
                    else:
                        if l[i+r][j+c]!='B':
                            count+=1
                        else:
                            count+=0
                
        if count>32:
            d.append(64-count)
        else:
            d.append(count)
                  
print(min(d)) 