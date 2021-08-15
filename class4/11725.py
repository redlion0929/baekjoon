import sys

def find_par(prev_node,cur_node):
    parent[cur_node] = prev_node
    if len(tree[cur_node]) == 1:
        return False
    else:
        return True
    
n = int(sys.stdin.readline().rstrip())

parent = [-1]*(n+1)
tree = {}

for i in range(n+1):
    tree[i] = []

for _ in range(n-1):
    j,k = map(int, sys.stdin.readline().rstrip().split())
    tree[j].append(k)
    tree[k].append(j)

start = 1
while True:
    for i in tree[start]:
        if find_par(start,i) == False:
            continue
        else:
        
            
print(parent)