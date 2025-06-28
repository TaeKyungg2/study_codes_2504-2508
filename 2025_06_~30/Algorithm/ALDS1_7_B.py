from dataclasses import dataclass

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

    def set_depth(self, node, depth):
        if node == None:
            return
        node.depth = depth
        if node.left != None:
            self.set_depth(node.left, depth + 1)
        if node.right != None:
            self.set_depth(node.right, depth + 1)

    def set_height(self, node):
        if node == None:
            return
        if node.left == None and node.right == None:
            node.height = 0
        elif node.left == None:
            node.height = self.set_height(node.right) + 1
        elif node.right == None:
            node.height = self.set_height(node.left) + 1
        else:
            node.height = max(self.set_height(node.left), self.set_height(node.right)) + 1
        return node.height

    def print_tree(self):
        for node in self.nodes:
            if node == None:
                continue
            print(f"""node {node.id}: parent = {node.parent.id if node.parent != -1 else -1}, sibling = {node.sibling.id if node.sibling != -1 else -1}, degree = {node.degree}, depth = {node.depth}, height = {node.height}, {node.type}""")

    def set_type(self, node):
        if node.parent == -1:
            node.type = "root"
        elif node.left == None and node.right == None:
            node.type = "leaf"
        else:
            node.type = "internal node"

    def set_sibling(self, node):
        if node.left == None and node.right == None:
            return
        if node.left != None and node.right != None:
            node.left.sibling = node.right
            node.right.sibling = node.left

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
if __name__ == "__main__":
    tree=build_tree()
    tree.set_depth(tree.root, 0)
    tree.set_height(tree.root)
    for node in tree.nodes:
        if node == None:
            continue
        tree.set_type(node)
    for node in tree.nodes:
        if node == None:
            continue
        tree.set_sibling(node)
    tree.print_tree()