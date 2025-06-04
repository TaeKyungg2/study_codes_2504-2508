class MyQueue:
    def __init__(self, size=10):
        if size<10: #최소 10이상
            size=10 
        self.size = size 
        self.queue = [None] * self.size
        self.front = 0 
        self.rear = 0
    
    def put(self, data):
        """
        rear 하나 증가시킨다음에 % self.size 로 나머지 구하고 
        그 위치에 데이터 넣기 
        """
        if self.isFull():
            print("queue is full")
            return 
        self.rear = (self.rear+1)%self.size
        self.queue[self.rear]=data

    def isEmpty(self):
        if self.rear==self.front:
            return True 
        return False 
    
    def isFull(self):
        if (self.rear+1)%self.size==self.front:
            return True 
        return False 

    def get(self): 
        """
        front 증가시켜서 그 위치값 반화하기     
        """
        if self.isEmpty():
            print("queue is empty")
            return None
        self.front = (self.front+1)%self.size 
        return self.queue[self.front]
    
    def peek(self):
        """
        front 증가시켜서 그 위치값 반화하기
        front자체는 바꾸면 안된다
        """
        if self.isEmpty():
            print("queue is empty")
            return None
        temp = (self.front+1)%self.size 
        return self.queue[temp]
#q=MyQueue()

#print(q.queue)
from random import randint
import asyncio
class Bank():
    number=MyQueue(20)

    @staticmethod
    async def Awindow():
        while True:
            num=Bank.number.get()
            if num==None:
                await asyncio.sleep(1)
                continue
            await asyncio.sleep(randint(1,3))
            print(f"A window{num} customer Done")

    @staticmethod
    async def Bwindow():
        while True:
            num=Bank.number.get()
            if num==None:
                await asyncio.sleep(1)
                continue
            await asyncio.sleep(randint(3,5))
            print(f"B window{num} customer Done")
            
    @staticmethod
    async def Cwindow():
        while True:
            num=Bank.number.get()
            if num==None:
                await asyncio.sleep(1)
                continue
            await asyncio.sleep(randint(3,5))
            print(f"C window{num} customer Done")

    @staticmethod
    async def bank():
        await asyncio.gather(
            Bank.Awindow(),
            Bank.Bwindow(),
            Bank.Cwindow()
        )

class Customer():
    num=100
    def __init__(self):
        self.num=Customer.num
        Customer.num+=1
        print(f"{self.num} customer visit.")
        Bank.number.put(self.num)

async def main():
    a=asyncio.create_task(Bank.bank())
    for i in range(1,100):
        human=Customer()
        await asyncio.sleep(1)
    await a
asyncio.run(main())





