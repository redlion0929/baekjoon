import sys
n = int(sys.stdin.readline().strip())
l = [int(sys.stdin.readline().strip()) for _ in range(n)]

def partition(arr,start,end) :
    pivot = arr[end]
    i = start-1
    for j in range(start, end):
        if arr[j]<pivot:
            i+=1
            tmp = arr[j]
            arr[j]=arr[i]
            arr[i]=tmp
    temp = arr[i+1]
    arr[i+1] = arr[end]
    arr[end] = temp
    return i+1

def quick_sort(arr,start, end):
    if start<end:
        p = partition(arr,start, end)
        quick_sort(arr,start,p-1)
        quick_sort(arr,p+1,end)

quick_sort(l,0,len(l)-1)
for i in l:
    print(i)