from MyQueue import MyQueue

q = MyQueue()

print(q.queue)
from random import randint
import asyncio


class Bank:
    number = MyQueue(20)

    @staticmethod
    async def Awindow():
        while True:
            num = Bank.number.get()
            if num == None:
                await asyncio.sleep(1)
                continue
            await asyncio.sleep(randint(1, 3))
            print(f"A window{num} customer Done")

    @staticmethod
    async def Bwindow():
        while True:
            num = Bank.number.get()
            if num == None:
                await asyncio.sleep(1)
                continue
            await asyncio.sleep(randint(3, 5))
            print(f"B window{num} customer Done")

    @staticmethod
    async def Cwindow():
        while True:
            num = Bank.number.get()
            if num == None:
                await asyncio.sleep(1)
                continue
            await asyncio.sleep(randint(3, 5))
            print(f"C window{num} customer Done")

    @staticmethod
    async def bank():
        await asyncio.gather(Bank.Awindow(), Bank.Bwindow(), Bank.Cwindow())


class Customer:
    num = 100

    def __init__(self):
        self.num = Customer.num
        Customer.num += 1
        print(f"{self.num} customer visit.")
        Bank.number.put(self.num)


async def main():
    a = asyncio.create_task(Bank.bank())
    for i in range(1, 100):
        human = Customer()
        await asyncio.sleep(1)
    await a


asyncio.run(main())
