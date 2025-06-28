
#fail...;.

class Node:
    def __init__(self, id):
        self.id=id
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

def divideRL(n):
    if Post[n+1] in end_nodes:return

    new_node=Node(Post[n+1])
    end_nodes[new_node.id]=new_node
    before_index=In.index(Post[n])
    new_index=In.index(Post[n+1])

    if before_index>new_index:
        end_nodes[Post[n]].left=new_node
    else:
        end_nodes[Post[n]].right=new_node

    if abs(before_index-new_index)==2:
        new_node.left=In[new_index-1]
        new_node.right=In[new_index+1]
        end_nodes[new_node.left.id]=new_node.left
        end_nodes[new_node.right.id]=new_node.right

def print_postorder(node):
    if node == None:return
    print_postorder(node.left)
    print_postorder(node.right)
    print("",node.id, end="")

if __name__ == "__main__":
    n=int(input())
    Post=list(map(int, input().split()))
    In=list(map(int, input().split()))
    end_nodes=[None]*(n+1)
    root=Node(Post[0])
    end_nodes[root.id]=root
    for i in range(1,n-1):
        divideRL(i)
    print_postorder(root)
