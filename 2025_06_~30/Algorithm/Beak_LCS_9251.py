def dynamic(fir,sec):
    dp=[]
    for i in range(len(fir)):
        dp.append([0]*(len(sec)))
    a,b=0,0
    for a in range(1,len(fir)):
        for b in range(1,len(sec)):
            if fir[a]==sec[b]:dp[a][b]=dp[a-1][b-1]+1
            else : dp[a][b]=dp[a-1][b] \
                if dp[a-1][b]>dp[a][b-1] else dp[a][b-1]

    print(dp[-1][-1])

fir=' '+input()
sec=' '+input()
dynamic(fir,sec)

