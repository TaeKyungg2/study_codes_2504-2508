

def CountingSort(A,B,k):
    C=[0]*(k+1)
    for i in A:
        C[i]+=1
    for i in range(1,k+1):
        C[i]+=C[i-1]
    for i in range(len(A)-1,-1,-1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]-=1

input_num = int(input())
A=list(map(int,input().split()))
B=[0]*input_num
CountingSort(A,B,max(A))

for i in range(input_num):
    if i == input_num-1:
        print(B[i])
    else:
        print(B[i],end=" ")