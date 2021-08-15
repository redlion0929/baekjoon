import sys

L = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()
H = 0
for i,j in enumerate(S):
    val = ord(j)-ord('a')+1
    H+=(val*(31**i))
    
print(H%1234567891)