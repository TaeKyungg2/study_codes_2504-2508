
def maxHeapify(A,i):
    l=2*i
    r=2*i+1
    big=i
    if l>=len(A):return
    if A[l]>A[big]:
        big=l
    if r<len(A) and A[r]>A[big]:
        big=r
    if big!=i:
        A[i],A[big]=A[big],A[i]
        maxHeapify(A,big)

def buildMaxHeap(A):
    for i in range(n//2,0,-1):
        maxHeapify(A,i)

n=int(input())
Heap=[None]+list(map(int,input().split()))
buildMaxHeap(Heap)
for i in range(1,n+1):
    print("",Heap[i],end="")
print()