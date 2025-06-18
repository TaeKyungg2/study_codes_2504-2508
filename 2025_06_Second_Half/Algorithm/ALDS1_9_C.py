
class Heap:
    def __init__(self):
        self.nums=[None]

    def insert(self,key):
        self.nums.append(key)
        index=len(self.nums)-1
        while index>1 and self.nums[index//2]<self.nums[index]:
            self.nums[index//2],self.nums[index]=self.nums[index],self.nums[index//2]
            index=index//2
        
    def extract_max(self):
        max=self.nums[1]
        self.change_child(1)
        return max
    
    def change_child(self,index):
        if index*2>=len(self.nums):
            self.nums[index]=-1
            return
        if index*2+1==len(self.nums) or self.nums[index*2]>self.nums[index*2+1]:
            self.nums[index],self.nums[index*2]=self.nums[index*2],self.nums[index]
            self.change_child(index*2)
        else:
            self.nums[index],self.nums[index*2+1]=self.nums[index*2+1],self.nums[index]
            self.change_child(index*2+1)
    
if __name__ == "__main__":
    heap=Heap()
    while True:
        command=input().split()
        if command[0]=="insert":
            heap.insert(int(command[1]))
        elif command[0]=="extract":
            print(heap.extract_max())
        elif command[0]=="end":
            break