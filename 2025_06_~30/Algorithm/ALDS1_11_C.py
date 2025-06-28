def RowToInt():
    nums=[]
    nums=list(map(int,input().split()))
    return nums

def NRowToInt():
    n=int(input())
    nums_=[None]
    for i in range(n):
        nums_.append(RowToInt())
    return nums_
import queue
qu=queue.Queue()
def BFS():
    global times
    while not qu.empty():
        now=qu.get()
        if times[now[0][0]]!=-1:continue
        times[now[0][0]]=now[1]
        for i in now[0][2:]:
            qu.put([gra[i],now[1]+1])

gra=NRowToInt()
times=[-1]*(len(gra))
qu.put([gra[1],0])
BFS()

for n in range(1,len(times)):
    print(f'{n} {times[n]}')
    n+=1

