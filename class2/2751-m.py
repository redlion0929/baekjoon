import sys
n = int(sys.stdin.readline().strip())
l = [int(sys.stdin.readline().strip()) for _ in range(n)]

def merge_sort(arr):
    if len(arr)<=1:
        return
    mid = (len(arr))//2
    m1 = arr[ : mid]
    m2 = arr[mid: ]
    merge_sort(m1)
    merge_sort(m2)
        
    i=0
    j=0
    k=0
    while ((i<len(m1))&(j<len(m2))):
        if m1[i]<m2[j]:
            arr[k]=m1[i]
            i+=1
            k+=1
        else:
            arr[k] = m2[j]
            j+=1
            k+=1
              
    while i<len(m1):
        arr[k]=m1[i]
        i+=1
        k+=1
                
    while j<len(m2):
        arr[k] = m2[j]
        j+=1
        k+=1
            
            
merge_sort(l)

for i in l:
    print(i)