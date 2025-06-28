def RowToInt():
    nums=[]
    nums=list(map(int,input().split()))
    return nums

def NRowToInt():
    n=int(input())
    nums_=[]
    for i in range(n):
        nums_.append(RowToInt())
    return nums_

def OutList(list):
    for i in list:
        print(i,end=' ')

def Out2list(list):
    for i in list:
        OutList(i)
        print()

