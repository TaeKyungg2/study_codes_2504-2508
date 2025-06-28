def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]
    L[n1] = float("inf")
    R[n2] = float("inf")
    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A


cnt = 0


def mergeSort(A, left, right):
    global cnt
    if left + 1 < right:
        mid = (left + right) // 2
        cnt += len(A[left:right])
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)


input_num = int(input())
input_list = list(map(int, input().split()))
mergeSort(input_list, 0, input_num)
for i in range(input_num):
    if i == input_num - 1:
        print(input_list[i])
    else:
        print(input_list[i], end=" ")
print(cnt)
