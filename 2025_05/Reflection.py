class MyType:
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y 
    def add(self):
        return self.x+self.y 
    
    def sub(self):
        return self.x-self.y 
    
    def mul(self):
        return self.x*self.y 
k=MyType(4,5)
for x in dir(MyType):
    if not x.startswith("__"):
        func=getattr(MyType,x)
        print(func.__name__)
        print(func(k))

import inspect
inspect.signature() # get pamamitor.
inspect.getmembers() #get members name.
inspect.isfunction() #inspect object is function.