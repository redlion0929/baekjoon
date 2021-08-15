import sys
n = int(sys.stdin.readline().strip())
l = [int(sys.stdin.readline().strip()) for _ in range(n)]

def max_heapify(a, i, heap_size):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if (left<heap_size):
        if (a[left]>a[largest]):
            largest = left
    if (right<heap_size):
        if (a[right]>a[largest]):
            largest = right
    if largest!=i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest, heap_size)
        
def build_max_heap(a):
    heap_size = len(a)
    for i in range(len(a)//2-1,-1,-1):
        max_heapify(a, i, heap_size)

def heap_sort(a):
    heap_size = len(a)
    build_max_heap(a)
    for i in range(len(a)-1,0,-1):
        a[i],a[0] = a[0], a[i]
        heap_size-=1
        max_heapify(a, 0, heap_size)
        
        
heap_sort(l)
for i in l:
    print(i)