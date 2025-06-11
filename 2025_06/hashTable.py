class HashTable:
    def __init__(self,num):
        self.table=[None]*num
        self.divNum=num

    def hashInsert(self,key,value=0):
        if self.table[self.hash(key)]==None:
            self.table[self.hash(key)]=LinkedList(key,value)
            return True
        else:
            self.collison(key,value)
            return True
    
    def hash(self,key):
        sum=0
        for i in key:
            sum+=ord(i)
        return sum%self.divNum
    
    def find(self,key):
        if self.table[self.hash(key)]==None:
            print("key not found")
            return True
        else:
            node=self.table[self.hash(key)].head
            while node.next!=None:
                print(node.key,":",node.value,end=" ")
                node=node.next
            print(node.key,":",node.value)

            return False
    def collison(self,key,value):
        self.table[self.hash(key)].add(key,value)
        return
    
    def printTable(self):
        node=Node()
        n=0
        for i in self.table:
            print(n,end=" > ")
            if i!=None:
                node=i.head
                while node.next!=None:
                    print(node.key,":",node.value,end=", ")
                    node=node.next
                print(node.key,":",node.value)
            else:
                print("None")
            n+=1

class LinkedList:
    def __init__(self,key,value):
        self.head=Node(key,value)
        self.tail=self.head

    def add(self,key,value):
        node=self.head
        while True:
            if node.key==key:
                print("key already exists")
                return False
            if node.next==None:break
            node=node.next
        node.next=Node(key,value)
        self.tail=node.next
        return True
        
class Node:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.next=None

if __name__=="__main__":
    myHash=HashTable(5)
    myHash.hashInsert("apple","사과")
    myHash.hashInsert("banana","바나나")
    myHash.hashInsert("cherry","체리")
    myHash.hashInsert("date","데이트")
    myHash.hashInsert("elderberry","엘더베리")
    myHash.hashInsert("fig","피그")
    myHash.hashInsert("apple","사과")
    myHash.hashInsert("apple","사과")
    myHash.hashInsert("eppla","과사")
    myHash.printTable()
    myHash.find("apple")
    myHash.find("banana")
    myHash.find("cherry")
    myHash.find("date")
    myHash.find("elderberry")
    myHash.find("fig")
    myHash.find("egg")


    
        