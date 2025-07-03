

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


def findLowCost(node):
    for i in range(2,len(node),2):
        if costs[node[i]]<costs[node[0]]+node[i+1]:continue
        heapq.heappush(WaitNode,(node[i+1],node[i],node[0]))
    if len(WaitNode)==0:return False,False,False
    return heapq.heappop(WaitNode)

import heapq

WaitNode=[]
infor=NRowToInt()
node=0
cost=0
costs=[float("inf")]*len(infor)
costs[0]=0
parent=0
while node is not False:
    new_cost=cost+costs[parent]
    if costs[node]>new_cost:
        costs[node]=new_cost
    cost,node,parent=findLowCost(infor[node])

for i,co in enumerate(costs):
    print(i,co)








        

