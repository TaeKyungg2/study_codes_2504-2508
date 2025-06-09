class Node:
    def __init__(self,data=None):
        self.data=data
        #self.child=[]
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end="\t")
        inorder(node.right) # become stack structure outo. cycle call.

def 

if __name__ == "__main__":
    tree = Tree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    tree.root.left.left.left = Node("G")
