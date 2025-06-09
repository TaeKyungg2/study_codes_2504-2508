from MyQueue import MyQueue

class Node:
    def __init__(self,data=None):
        self.data=data
        #self.child=[]
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None

    def insertNode(self, data=None):
        newNode=Node(data) #to add at tree, make node.
        if self.root==None:
            self.root=newNode

    def levelorder(self): # BFS
        qu=MyQueue(100)
        qu.put(self.root)
        while not qu.isEmpty():
            temp=qu.get()
            print(temp.data,end='\t')
            if temp.left is not None:
                qu.put(temp.left)
            if temp.right is not None:
                qu.put(temp.right)
    def addNode(self,parent=None,left=True,data=None): # if bLeft is True, add left. False,add right.
        temp=Node(data)
        if parent==None : self.root=temp
        else: 
            if left:parent.left=temp
            else:parent.right=temp
        return temp
def makeTree1():
    tree=Tree()
    root=tree.addNode(data="A")
    level1=tree.addNode(root,True,"B")
    level2=tree.addNode(root,False,"C")

    tree.addNode(level1,True,"D")
    tree.addNode(level1,False,"E")

    tree.addNode(level2,True,"F")
    tree.addNode(level2,False,"G")
    return tree

def makeTree(data):
    tree=Tree()
    for i in data:
        qu=MyQueue()
        qu.put(tree.root)
        bleft=True
        temp=None
        while not qu.isEmpty() and qu.peek() is not None:
            temp=qu.get()
            if temp.left is not None:
                qu.put(temp.left)
                bleft=False
            if temp.right is not None:
                qu.put(temp.right)
                bleft=True
        tree.addNode(temp,bleft,data=i)
    return tree

def myMakeTree(data):
    tree=Tree()
    qu=MyQueue()
    qu.put(tree.addNode(None,True,data[0]))
    for i in data:
        if i==data[0]:continue
        parent=qu.get()
        if parent.left==None:node=tree.addNode(parent,True,i)
        else: node=tree.addNode(parent,False,i)
        qu.put(node)
    return tree
    

def inorder(node):
        if node:
            inorder(node.left)
            print(node.data, end="\t")
            inorder(node.right) # become stack structure outo. cycle call.

def postorder(node):
    if node:
        inorder(node.left)
        inorder(node.right)
        print(node.data, end="\t")

def preorder(node):
        if node:
            print(node.data, end="\t")
            inorder(node.left)
            inorder(node.right)





if __name__ == "__main__":
    tree = myMakeTree("ABCDEFGHI")
    # tree.root = Node("A")
    # tree.root.left = Node("B")
    # tree.root.right = Node("C")
    # tree.root.left.left = Node("D")
    # tree.root.left.right = Node("E")
    # tree.root.right.left = Node("F")
    # tree.root.left.left.left = Node("G")

    print("inorder : ",end="\t")
    inorder(tree.root)
    print()

    print("preorder : ",end="\t")
    preorder(tree.root)
    print()

    print("postorder : ",end="\t")
    postorder(tree.root)
    print()

    print("levelorder : ",end='\t')
    tree.levelorder()