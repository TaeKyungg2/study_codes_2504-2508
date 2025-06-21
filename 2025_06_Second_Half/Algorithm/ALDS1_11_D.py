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
    flag=False
    for i in range(len(friend[node])):
        if visit[i]==True : return
        else : visit[i]=True
        if friend[node][i]==f:return True
        else : flag=flag or dfs(friend[node][i],f)
    return flag
fri,num=NRowToInt2()
query=NRowToInt()
friend=[[] for i in range(num)]

for i in fri:
    friend[i[0]].append(i[1])
    friend[i[1]].append(i[0])
for i in query:
    visit=[False]*num
    if dfs(i[0],i[1]):print('yes')
    else : print('no')
