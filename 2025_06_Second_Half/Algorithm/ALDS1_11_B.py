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
arr=NRowToInt()
time=[[0,0] for _ in range(len(arr))]
ii=1
def DFSarr(node):
    global ii,arr,time
    if time[node-1][0]!=0 : return
    time[node-1][0]=ii
    ii+=1
    for i in arr[node-1][2:]:
        DFSarr(i)
    
    time[node-1][1]=ii
    ii+=1

DFSarr(arr[0][0])
i=1
flag=[0,0] in time
while flag:
    if time[i][0]==0:
        DFSarr(arr[i][0])
        if [0,0] not in time:break
    i+=1
    i%=len(time)

for i in arr:
    print(f'{i[0]} {time[i[0]-1][0]} {time[i[0]-1][1]}')