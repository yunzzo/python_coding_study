n = int(input())
A = [0, ]
for _ in range(n):
    A.append(int(input()))

def heapSort(A):
    heapSize = n
    A = buildMaxHeap(A)
    for i in range(n, 1, -1):
        A[1] , A[i] = A[i] , A[1]
        heapSize -= 1
        A = maxHeapify(A,1,heapSize)
    return A

def buildMaxHeap(A):
    for i in range(n//2, 0, -1):
        A = maxHeapify(A,i,n)
    return A

def maxHeapify(A,i,heapSize):
    l = left(i)
    r = right(i)
    if l <= heapSize and A[l] > A[i]:
        largest = l
    else: 
        largest = i
    if r <= heapSize and A[r] > A[largest]:
        largest = r
    if largest != i :
        A[i] , A[largest] = A[largest], A[i]
        maxHeapify(A,largest,heapSize)
    return A

def parent(i):
    return i//2
def left(i):
    return 2*i
def right(i):
    return 2*i +1

for i in heapSort(A)[1:]:
    print(i)