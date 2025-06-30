


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
    
nodes=NRowToInt()
graph=[]
for node in nodes:
    graph.append([0]*((len(node)-2)//2))
    for i in range(0,(len(node)-2)//2,2):
        graph[node[0]][i]=node[i+1]
price=[None]*len(nodes)
        

