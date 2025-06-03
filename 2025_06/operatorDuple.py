# class MyType:
#     def __init__(self, x=0,y=0):
#         self.x=x
#         self.y=y
#     def __add__(self,other): # + function.
#         return MyType(self.x+other.x,self.y+other.y)
#     def __str__(self): #return should be str. print().
#         return f"x:{self.x} y:{self.y}"
#     def __sub__(self,other):
#         return MyType(self.x-other.x,self.y-other.y)
#     def __mul__(self,other):
#         return MyType(self.x*other.x,self.y*other.y)
#     def __truediv__(self,other):
#         return MyType(self.x/other.x,self.y/other.y)
# a=MyType(4,5)
# b=MyType(2,3)
# print(a+b)
# print(int.__dict__)

class MyList:
    def __init__(self,data):
        self.data=list(data)
    def __str__(self):
        return f"MyList({self.data})"

    def __getitem__(self,index):
        if index>=0 and index<len(self.data):
            return self.data[index]
        else: return 'no'
    def __setitem__(self,index,value):
        self.data[index]=value

my=MyList((1,3,5,7,8))
print(my)
print(my[2])
my[2]=100
print(my[2])
print(my[100])
