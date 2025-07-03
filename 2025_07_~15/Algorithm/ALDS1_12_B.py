

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

def makeGra():
    graph=[]
    for i in infor:
        graph.append([float("inf")]*len(infor))
    for node in infor:
        for i in range(2,len(node)-1,2):
            graph[node[0]][node[i]]=node[i+1]
    return graph

def findLowCost(node):
    for i in range(2,len(node),2):
        if node[i] in visit:continue
        heapq.heappush(WaitNode,(node[i+1],node[i]))
    if len(WaitNode)==0:return False,False
    return heapq.heappop(WaitNode)

import heapq

visit=set()
WaitNode=[]
infor=NRowToInt()
graph=makeGra()
node=0
cost=0
costs=[float("inf")]*len(infor)
costs[0]=0
while node is not False:
    visit.add(node)
    new_cost=cost+costs[node]
    if costs[node]>new_cost:
        costs[node]=new_cost
    cost,node=findLowCost(infor[node])

for i,co in enumerate(costs):
    print(i,co)








        

