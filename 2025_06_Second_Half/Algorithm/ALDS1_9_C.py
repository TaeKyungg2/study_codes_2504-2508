nums=[None]

def insert(key):
    nums.append(key)
    index=len(nums)-1
    while nums[index//2]<nums[index]:
        nums[index//2],nums[index]=nums[index],nums[index//2]
        index=index//2
    
H=0
def extractMax(A):
    H+=1
    max=A[1]
    A[1]=A[H]
    del A[H]
    return max

while True:
    command=input().split()
    if command[0]=="insert":
        insert(int(command[1]))
    elif command[0]=="extract":
        print(extractMax(nums))
    elif command[0]=="end":
        break