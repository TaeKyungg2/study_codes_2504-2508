

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
        graph.append([None]*i[1]*2)
    for node in infor:
        print(graph[node[0]])
        for i in range(2,len(node)-2,2):
            graph[node[0]][i]=node[i+1]
    costs=[None]*len(infor)
    for i in range(2,len(infor)-2,2):
        costs[infor[i][0]]=infor[i]
    return graph,costs

def findLowCost(node):
    minCost=float("inf")
    lowNode=None
    for i in range(2,len(node)-2,2):
        if minCost<node[i+1]:
            minCost=node[i+1]
            lowNode=node[i]
    return lowNode

infor=NRowToInt()
graph,costs=makeGra()
costs[0]=0
node=0
while node is not None:
    cost=costs[node]
    for i in range(2,infor[node]-1,2):
        new_cost=cost+infor[node][i+1]
        if costs[i]>new_cost:
            costs[i]=new_cost
    
    node=findLowCost(infor[node])
for i,co in enumerate(costs):
    print(i,co)








        

