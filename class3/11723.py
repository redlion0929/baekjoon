import sys
n = int(sys.stdin.readline().rstrip())
s = set()

def add(x):
    s.add(x)

def check(x):
    if x in s:
        return True
    else:
        return False

def remove(x):
    if check(x):
        s.remove(x)
    
def toggle(x):
    if check(x):
        remove(x)
    else:
        add(x)

for _ in range(n):
    line = sys.stdin.readline().rstrip()
    op = line.split()[0]
    
    if op =="add":
        add(int(line.split()[1]))
    
    elif op == "remove":
        remove(int(line.split()[1]))
        
    elif op == "check":
        if (check(int(line.split()[1]))):
            print(1)
        else:
            print(0)
        
    elif op == "toggle":
        toggle(int(line.split()[1]))
        
    elif op == "all":
        s = set(range(1,21))
    
    elif op == "empty":
        s = set()
        
    else:
        exit()