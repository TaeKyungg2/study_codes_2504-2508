class Node():
    def __init__(self,data=None):
        self.next=None
        self.prev=None
        self.data=data
class DoubleLikedList:
    def __init__(self):
        self.tail=Node()
        self.head=Node()
        self.head.next=self.tail
        self.tail.next=self.tail
        self.head.prev=self.head
        self.tail.prev=self.head
    def insertHead(self,data):
        temp=Node(data)
        temp.next=self.head.next
        temp.prev=self.head
        self.head.next=temp
        self.head.next.prev=temp
    def printNext(self):
        t=self.head.next
        while t!=self.tail:
            print(f"{t.data} ",end="")
            t=t.next
        print()

    def printPrev(self):
        t=self.tail.prev
        while t!=self.head:
            print(f"{t.data} ",end="")
            t=t.prev
        print()

    def insertTail(self,data):
        temp=Node(data)
        temp.next=self.tail
        temp.prev=self.tail.prev
        self.tail.prev.next=temp
        self.tail.prev=temp
    def deleteHead(self):
        if self.head.next == self.tail:
            return
        self.head.next=self.head.next.next
        self.head.next.prev=self.head
    def deleteTail(self):
        if self.tail.prev==self.head:
            return
        self.tail.prev=self.tail.prev.prev
        self.tail.prev.next=self.tail

dlist=DoubleLikedList()
dlist.insertHead(1)
dlist.insertHead(4)
dlist.insertHead(7)
dlist.insertHead(2)
dlist.insertHead(4)
dlist.insertHead(1)
dlist.insertHead(7)
dlist.insertHead(9)
dlist.insertHead(3)
dlist.printPrev()
dlist.printNext()
dlist.insertTail(12)
dlist.insertTail(21)
dlist.insertTail(56)
dlist.insertTail(78)
dlist.insertTail(34)
dlist.insertTail(23)

dlist.printPrev()
dlist.deleteHead()
dlist.deleteTail()
dlist.printNext()
