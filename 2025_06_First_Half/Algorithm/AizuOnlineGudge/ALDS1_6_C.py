
def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [[0 for _ in range(2)] for _ in range(n1+1)]
    R = [[0 for _ in range(2)] for _ in range(n2+1)]
    for i in range(n1):
        L[i] = A[left + i].copy()
    for i in range(n2):
        R[i] = A[mid + i].copy()
    L[n1][1] = float("inf")
    R[n2][1] = float("inf")
    i = 0
    j = 0
    for k in range(left, right):
        if L[i][1] <= R[j][1]:
            A[k] = L[i].copy()
            i += 1
        else:
            A[k] = R[j].copy()
            j += 1

def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)




def partition(A,p,r):
    x = A[r][1]
    i = p-1
    for j in range(p,r):
        if A[j][1] <= x:
            i += 1
            A[i],A[j] = A[j].copy(),A[i].copy()
    A[i+1],A[r] = A[r].copy(),A[i+1].copy()
    return i+1
def quickSort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)
    
input_num = int(input())
input_list = []
for i in range(input_num):
    input_list.append(input().split())
    input_list[i][1] = int(input_list[i][1])
input_list_copy = input_list.copy()

mergeSort(input_list_copy, 0, input_num)
quickSort(input_list,0,input_num-1)

if input_list == input_list_copy:
    print("Stable")
else:
    print("Not stable")

for i in range(input_num):
    print(input_list[i][0],input_list[i][1])






