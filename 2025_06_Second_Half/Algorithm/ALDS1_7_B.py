class Node:
    def __init__(self, id):
        self.id = id
        self.right = None
        self.left = None
        self.sibling = -1
        self.parent = None
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = None


noFinds = []


class Tree:
    def __init__(self, n):
        self.root = None
        self.nodes = [None] * (n)

    def insert(self, node):
        if self.root == None:
            self.root = node
            node.parent = -1
            return

        find_node = self.find_node(node.id)
        if find_node == None:
            childs.append(node)
            return
        if find_node.left == node.id:
            find_node.left = node
            node.parent = find_node
        else:
            find_node.right = node
            node.parent = find_node
        self.nodes[node.id] = node
        return True

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
        return node.height

    def print_tree(self):
        for node in self.nodes:
            print(
                f"""node {node.id}: parent = {node.parent.id if node.parent != -1 else -1}, sibling = {node.sibling.id if node.sibling != -1 else -1}, degree = {node.degree}, depth = {node.depth}, height = {node.height}, {node.type}"""
            )

    def set_type(self, node):
        if node.parent == -1:
            node.type = "root"
        elif node.left == None and node.right == None:
            node.type = "leaf"
        else:
            node.type = "internal node"

    def find_node(self, id):
        for node in self.nodes:
            if node == None:
                continue
            if node.right == id or node.left == id:
                return node
        return None

    def set_sibling(self, node):
        if type(node.left) == int:
            return
        if type(node.right) == int:
            return
        if node.left == None and node.right == None:
            return
        if node.left != None and node.right != None:
            node.left.sibling = node.right
            node.right.sibling = node.left


n = int(input())
childs = [None] * (n)
tree = Tree(n)
for i in range(n):
    childs[i] = list(map(int, input().split()))

while True:
    node = Node(childs[0][0])
    node.left = int(childs[0][1]) if childs[0][1] != -1 else None
    node.right = int(childs[0][2]) if childs[0][2] != -1 else None
    if childs[0][1] != -1 and childs[0][2] != -1:
        node.degree = 2
    elif childs[0][1] != -1 or childs[0][2] != -1:
        node.degree = 1
    else:
        node.degree = 0
    tree.nodes[childs[0][0]] = node
    if tree.insert(node):
        childs.pop(0)
    if len(childs) == 0:
        break
tree.set_depth(tree.root, 0)
tree.set_height(tree.root)
for node in tree.nodes:
    tree.set_type(node)
for node in tree.nodes:
    tree.set_sibling(node)
tree.print_tree()


# childs[1].sibling=childs[2]
# childs[2].sibling=childs[1]
