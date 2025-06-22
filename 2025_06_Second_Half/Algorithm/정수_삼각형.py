
def solution(triangle):
    def dyna(n,m,sum):
        if sum_tra[n][m]!=0:
            return sum_tra[n][m]
        else:
            sum+=triangle[n][m]
            sum_tra[n][m]=\
                sum if n==len(triangle)-1 else \
                max(dyna(n+1,m,sum),dyna(n+1,m+1,sum))
            return sum_tra[n][m]
    answer = 0
    sum_tra=[]
    for i in range(len(triangle)):
        sum_tra.append([0]*(i+1))
    answer=dyna(0,0,0)
    return answer

print(solution([[7], [3, 8], [8, 1, 0]\
        , [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
