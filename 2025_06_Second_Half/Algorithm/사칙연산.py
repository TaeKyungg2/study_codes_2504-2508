# 1 2 3 4 ->5  length-1==len
#     len-1(2블록)+len-2(3블록)+1(3블록의 자식)
# 1 2 3 4 5 ->    len=4
#     len-1(2블록)+len-2(3블록)+len-3(4블록)
# 3+2+1
# 3(1)    
# 4(2+1+1)

# f=시그마 1~len-1 + 시그마(시그마 1~len-1)

# - 가 있어야 괄호 의미가 있다.
class Pairs():
    def __init__(self):
        self.p=set()
def solution(arr):
    answer = -1
    def choose(o,t,pairs):
        if t-o<2:
            return
        pairs.p.append((o,t))
        if pairs in dict:
            return
        for i in range(o+1,t):
            choose(i,t,pairs)

            
    pairs=Pairs()
    choose(1,len(arr),pairs)

    return answer
cal={}
def calcul(str,pairs):
    if pairs in cal : return cal[pairs]
    
