import sys
sys.setrecursionlimit(1000000)
def NRowToInt2():
    n,m=tuple(map(int,input().split()))
    nums_=[]
    for i in range(m):
        nums_.append(RowToInt())
    return nums_,n
    
def NRowToInt():
    n=int(input())
    nums_=[]
    for i in range(n):
        nums_.append(RowToInt())
    return nums_

def RowToInt():
    nums=[]
    nums=list(map(int,input().split()))
    return nums

def dfs(node,f):
    global visit
    visit[node]=True
    if f in friend[node]:return True
    for i in friend[node]:
        if visit[i]==True : continue
        if dfs(i,f): return True
    return False
fri,num=NRowToInt2()
query=NRowToInt()
friend=[set() for i in range(num)]

for i in fri:
    friend[i[0]].add(i[1])
    friend[i[1]].add(i[0])
for i in query:
    visit=[False]*num
    if dfs(i[0],i[1]):print('yes')
    else : print('no')

#give color all mans and execute query o(1)