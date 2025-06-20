n=int(input())
matrix=[]
answer=[]
for i in range(n):
    gra=list(map(int, input().split()))
    matrix=[0]*n
    for j in range(gra[1]):
        matrix[gra[2+j]-1]=1
    answer.append(matrix)
    
for i in range(len(answer)):
    for j in range(len(answer[i])):
        print(answer[i][j],end='')
        if j==len(answer[i])-1:continue
        print(' ',end='')
    print()



