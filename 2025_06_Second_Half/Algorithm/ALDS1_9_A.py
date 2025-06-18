n=int(input())
heap=[None]+list(map(int,input().split()))
for i in range(1,n+1):
    print(f"node {i}: key = {heap[i]},",end="")
    if i!=1:
        print(f" parent key = {heap[i//2]},",end="")
    if i*2<=n:
        print(f" left key = {heap[i*2]},",end="")
    if i*2+1<=n:
        print(f" right key = {heap[i*2+1]},",end="")
    print()
