#https://school.programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):
    def dyna(n,m):
        if sum_tra[n][m]!=0:
            return sum_tra[n][m]
        else:
            if n!=len(triangle)-1 :
                v1=dyna(n+1,m)
                v2=dyna(n+1,m+1)
                sum_tra[n][m]=max(v1,v2)+triangle[n][m]
                return sum_tra[n][m]
            else:
                return triangle[n][m]
    answer = 0
    sum_tra=[]
    for i in range(len(triangle)):
        sum_tra.append([0]*(i+1))
    answer=dyna(0,0)
    return answer

print(solution([[7], [3, 8], [8, 1, 0]\
        , [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
