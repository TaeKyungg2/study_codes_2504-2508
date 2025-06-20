from dataclasses import dataclass
from re import X
dp=[]
fir=' '+input()
sec=' '+input()
for i in range(len(fir)):
    dp.append([0]*(len(sec)))
a,b=0,0

result=[]
ch=[]
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __lt__(self,other):
        if self.x<other.x and self.y<other.y:
            return True
        return False
        
for a in range(1,len(fir)):
    for b in range(1,len(sec)):
        if fir[a]==sec[b]:
            p=point(a,b)
            for i in hp:
                if i<p:ch.append(fir[a])


            # result+=fir[a]
            dp[a][b]=dp[a-1][b-1]+1
        else : dp[a][b]=dp[a-1][b] \
            if dp[a-1][b]>dp[a][b-1] else dp[a][b-1]

print(dp[-1][-1])
print(result)