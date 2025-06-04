def solution(nodes, edges):
    answer = []
    nodeGroup=[]
    rootNum=0
    for i in nodes:
        nodes%2==0
    n=0
    while True:
        n=edges[n][0]
        del edges[n]
    return answer

def find(pair,edges):
    finds=list(filter(lambda x : x[1]==pair[1] or x[0]==pair[1] or x[1]==pair[0] or x[0]==pair[0],edges))
    for i in finds:
        find(i)
    