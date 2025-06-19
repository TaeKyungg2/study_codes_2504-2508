def dynamic(fir,sec):
    dp=[len(fir)*[0]]*len(sec)
    a,b=0,0
    match=False
    for j in sec:
        b=0
        match=False
        for z in fir:
            if match : 
                dp[a][b]=dp[a][b-1]
                continue
            x=1 if j==z else 0
            if j==z : match=True
            if j==z and a!=0 and b!=0:dp[a][b]=dp[a-1][b-1]+1
            elif j==z and a!=0 : dp[a][b]=dp[a-1][b]+1
            elif j==z and b!=0: dp[a][b]=dp[a][b-1]+1
            elif a==0 and b==0 : dp[a][b]=x
            elif a==0 : dp[a][b]=dp[a][b-1]
            elif b==0 : dp[a][b]=dp[a-1][b]
            else : dp[a][b]=dp[a-1][b] if dp[a-1][b]>dp[a][b-1] else dp[a][b-1]
            b+=1
        a+=1
    result.append(dp[-1][-1])
result=[]

n=int(input())
for i in range(n):
    fir=input()
    sec=input()
    dynamic(fir,sec)
for i in result:
    print(i)

