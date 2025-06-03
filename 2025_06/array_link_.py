class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=Node #next Node's address.
class MyList:
    def __init__(self):
        self.head=Node() # no use.
        self.tail= Node() # no use.
        self.head.next=self.tail
        self.tail.next=self.tail

    def insertHead(self,data):
        temp=Node(data)
        temp.next=self.head.next
        self.head.next=temp

    def print(self):
        print(self.head.next.data)
        print(self.head.next.next.data)
        print(self.head.next.next.next.data)

    def print2(self): #don't change value of head,tail
        #Node for trace.
        trace=self.head.next
        while trace!=self.tail:
            print(trace.data)
            trace=trace.next

    def deleteHead(self):
        if self.head.next==self.tail:
            return
        self.head.next=self.head.next.next

    def delecteAll(self):
        self.head.next=self.tail

    def insertOrder(self,data):
        temp=Node(data)
        t1=self.head.next
        t2=self.head
        while t1!=self.tail:
            if t1.data.compare(temp,t1):
                t1=t1.next
                t2=t2.next
            else : break
        temp.next=t1
        t2.next=temp

# my.deleteHead()
# my.print2()
#double linked list - Have twe link. prev,next.
#circle linked list - no use.



class Book:
    def __init__(self,title="",publisher="",author=""):
        self.title=title
        self.publisher=publisher
        self.author=author
    def __gt__(self,other):
        if self.title>other.title:
            return True
        return False
    def __str__(self):
        return f"{self.title} {self.publisher} {self.author}"
    
    def compare(self,A,B):
        if A.data.title>B.data.title: return True
        else : return False


# print( Book("마법사의돌", "조앤롤링", "해냄") > 
#        Book("마법사의돌", "조앤롤링", "해냄"))
# print( Book("마법사의돌", "조앤롤링", "해냄") > 
#        Book("그리고아무도없었다", "아가사크리스티", "해냄"))
my=MyList()

my.insertOrder(Book('A'))
my.insertOrder(Book('C'))
my.insertOrder(Book('B'))
my.insertOrder(Book('A'))
my.insertOrder(Book('R'))
my.insertOrder(Book('Z'))
my.insertOrder(Book('E'))
my.print2()
