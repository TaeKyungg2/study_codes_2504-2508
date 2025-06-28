from dataclasses import dataclass, field
@dataclass
class Node:
    id:int
    edges: list = field(default_factory=list)
def see(node):
    pass

n=int(input())
li=[]
for i in range(n):
    li=list(map(int, input().split()))
    node=Node(i+1)
    for j in range(li[1]):

