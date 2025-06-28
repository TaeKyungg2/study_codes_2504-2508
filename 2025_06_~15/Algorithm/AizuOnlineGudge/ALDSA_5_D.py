count = 0  # no end....


def partition(A, p, r):
    global count
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            count += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    if A[i + 1] != A[r] and i + 1 != r:
        count += 1
    return i + 1


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


input_num = int(input())
arr = list(map(int, input().split()))
quickSort(arr, 0, input_num - 1)
print(count)
