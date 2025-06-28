class Node:
    def __init__(self, id):
        self.id = id
        self.right = None
        self.left = None
        self.sibling = -1
        self.parent = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = None
    def __eq__(self, other):
        if other == None:
            return False
        if type(other)==int:return self.id == other
        return self.id == other.id

class Tree:
    def __init__(self, n):
        self.root = None
        self.nodes = [None] * n

from collections import deque

def build_tree():
    n = int(input())
    nodes_id = deque()
    IsRoot=set()
    Del=set()
    for i in range(n):
        temp=list(map(int, input().split()))
        IsRoot.add(temp[0])
        Del.add(temp[1])
        Del.add(temp[2])
        IsRoot-=Del
        nodes_id.append(temp)
    big=max(nodes_id,key=lambda x:x[0])[0]
    tree = Tree(big+1)
    root=IsRoot.pop()
    tree.nodes[root]=Node(root)
    tree.root=tree.nodes[root]
    while True:
        node = Node(nodes_id[0][0])
        if node in tree.nodes:
            if nodes_id[0][1] != -1:
                tree.nodes[node.id].degree += 1
                tree.nodes[node.id].left = Node(nodes_id[0][1])
                tree.nodes[nodes_id[0][1]] = tree.nodes[node.id].left
                tree.nodes[node.id].left.parent = tree.nodes[node.id]
            if nodes_id[0][2] != -1:
                tree.nodes[node.id].degree += 1
                tree.nodes[node.id].right = Node(nodes_id[0][2])
                tree.nodes[nodes_id[0][2]] = tree.nodes[node.id].right
                tree.nodes[node.id].right.parent = tree.nodes[node.id]
            nodes_id.popleft()
        else :
            this_node=nodes_id.popleft()
            nodes_id.append(this_node)
        if len(nodes_id) == 0:
            break
    return tree

tree=build_tree()

def print_preorder(node):
    if node == None:return
    print("",node.id, end="")
    print_preorder(node.left)
    print_preorder(node.right)

def print_inorder(node):
    if node == None:return
    print_inorder(node.left)
    print("",node.id, end="")
    print_inorder(node.right)

def print_postorder(node):
    if node == None:return
    print_postorder(node.left)
    print_postorder(node.right)
    print("",node.id, end="")


if __name__ == "__main__":
    print("Preorder")
    print_preorder(tree.root)
    print()
    print("Inorder")
    print_inorder(tree.root)
    print()
    print("Postorder")
    print_postorder(tree.root)
    print()