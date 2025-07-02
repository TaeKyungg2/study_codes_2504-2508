import heapq

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
    
def GoSmall(node):
    global box,visit,sum
    visit[node]=True
    for i,pri in enumerate(A[node]):
        if pri==-1:continue
        heapq.heappush(box,(pri,i))
    
    while len(box)>0:
        pri,next=heapq.heappop(box)
        if visit[next]:continue
        sum+=pri
        GoSmall(next)

A=NRowToInt()
box=[]
visit=[False]*len(A)
sum=0
GoSmall(0)
print(sum)

