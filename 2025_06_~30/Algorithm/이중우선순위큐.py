#https://school.programmers.co.kr/learn/courses/30/lessons/42628
import heapq
def solution(operations):
    answer = []
    h=[]
    for i in operations:
        if i[0]=='I':
            n=i.split()
            heapq.heappush(h,int(n[1]))
        elif i=='D -1' and len(h)!=0:
            heapq.heappop(h)
        elif len(h)!=0 :
            h.sort()
            h.pop()
    if h==[]:answer=[0,0]
    elif len(h)==1:
        min=heapq.heappop(h)
        answer=[min,min]
    else : 
        answer=[heapq.nlargest(1,h)[0],heapq.heappop(h)]

    return answer
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
