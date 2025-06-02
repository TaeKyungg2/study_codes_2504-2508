class MyStack:
    def __init__(self,size=10):
        if size<10:self.size=10
        self.stack=[]
        for i in range(0,size):
            self.stack.append(0)
        self.top=-1
        self.size=size
    def isFull(self):
        if self.size-1 == self.top : return True
        else: return False
    def push(self,data):
        if self.isFull():
            print(f"stack can't eat {data}")
            return
        self.top+=1
        self.stack[self.top]=data
    def print(self):
        for i in range(0,self.size):
            print(self.stack[i],end=" ")
        print()
    def pop(self):
        if self.isEmpty():
            return 'Stack empty'
        temp=self.stack[self.top]
        self.stack[self.top]=0
        self.top-=1
        return temp
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    def peek(self):
        if self.isEmpty():
            print('can\'t peek')
            return
        return self.stack[self.top]
k=MyStack(12)
k.push('a')
k.push('b')
k.push('c')
k.push('d')
k.push('e')
k.push('f')
k.push('g')
k.push('h')
k.push('i')

def reverse(stack):
    for i in range(0,stack.top+1):
        print(stack.pop(),end='')

reverse(k)


