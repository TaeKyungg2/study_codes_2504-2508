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
        for i in range(o+1,t):
            choose(i,t,pairs)
            
    pairs=Pairs()
    choose(1,len(arr),pairs)
    def calcul(pairs,arr):
        expr=arr.copy()
        for i in  pairs.p:
            add_paren(i,expr)
            c=expr[2*i[0]-2:2*i[1]-1]
            c_str=''.join(c)
            if c_str in cal: return cal[c_str]
            result=eval(c_str)
            cal[c_str]=result
            expr=next_calc(expr,i,result)
            if len(expr)==1:
                return expr[0]
        return calcul(pairs,expr)

    def add_paren(tu,arr):
        arr[2*tu[0]-2]+='('
        arr[2*tu[1]-1]+=')'
        return arr

    def next_calc(arr,tu,result):
        arr[2*tu[0]-2]=arr[2*tu[0]-2].split(' ')[0]
        arr[2*tu[1]-1]=result
        for i in range(2*tu[0]-1,2*tu[1]-1):
            arr[i]= ''
        return arr

    return answer
cal={}
