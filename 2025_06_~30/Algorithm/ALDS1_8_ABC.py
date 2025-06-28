class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,key):
        new_node=Node(key)
        if self.root is None:
            self.root=new_node
            return
        current=self.root
        while True:
            if key<current.key:
                if current.left is None:
                    current.left=new_node
                    new_node.parent=current
                    break
                current=current.left
            elif key>current.key:
                if current.right is None:
                    current.right=new_node
                    new_node.parent=current
                    break
                current=current.right
            else : return
            
    def find(self,key):
        current=self.root
        while current is not None:
            if key<current.key:
                current=current.left
            elif key>current.key:
                current=current.right
            else:
                return "yes",current
        return "no",current
    def delete(self,key):
        flag,find_node=self.find(key)
        isLeft=False
        if flag=="no":return
        if find_node.parent.left==find_node:
            isLeft=True
        if find_node.left is None and find_node.right is None:
            if isLeft:find_node.parent.left=None
            else:find_node.parent.right=None
        elif find_node.left is None:
            find_node.right.parent=find_node.parent
            if isLeft:find_node.parent.left=find_node.right
            else:find_node.parent.right=find_node.right
        elif find_node.right is None:
            find_node.left.parent=find_node.parent
            if isLeft:find_node.parent.left=find_node.left
            else:find_node.parent.right=find_node.left
        else:
            find_node.key=find_node.right.key
            self.delete(find_node.right.key)

def print_preorder(node):
    if node == None:return
    print("",node.key, end="")
    print_preorder(node.left)
    print_preorder(node.right)

def print_inorder(node):
    if node == None:return
    print_inorder(node.left)
    print("",node.key, end="")
    print_inorder(node.right)

if __name__ == "__main__":
    n=int(input())
    tree=BinarySearchTree()
    for i in range(n):
        command=input().split()
        if command[0]=="insert":
            tree.insert(int(command[1]))
        elif command[0]=="print":
            print_inorder(tree.root)
            print()
            print_preorder(tree.root)
            print()
        elif command[0]=="find":
            print(tree.find(int(command[1]))[0])
        elif command[0]=="delete":
            tree.delete(int(command[1]))
