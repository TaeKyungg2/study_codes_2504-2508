class Tree:  # no complete
    def __init__(self):
        self.root = None

    def find_node(self, id, node, depth):  # return node,depth
        result = (node, depth)
        for i in node.childs:
            if i.id == id:
                return i, depth
            result = self.find_node(id, i, depth + 1)
        return result

    def print_tree(self, n):
        for i in range(n):
            node, depth = self.find_node(i, self.root, 0)
            if node.parent == -1:
                type = "root"
            elif len(node.childs) == 0:
                type = "leaf"
            else:
                type = "internal node"
            print(f"""node {node.id}: parent = {node.parent}, 
                    depth = {depth}, 
                    type = {type}, {node.childs}""")


class Node:
    def __init__(self, id):
        self.id = id
        self.childs = []
        self.parent = None


n = int(input())
tree = Tree()

for i in range(n):
    node = Node(i)
    if tree.root == None:
        tree.root = node
        tree.root.parent = -1
    node.parent, depth = tree.find_node(node.id, node, 0)
    if node.parent == -1:
        tree.root = node
        node.parent = -1
    elif node.parent == -2:
        pass
    temp = list(map(int, input().split()))
    for j in temp[1:]:
        c_node = Node(j)
        node.childs.append(c_node)
        c_node.parent = node.id

tree.print_tree(n)
