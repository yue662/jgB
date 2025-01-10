t,k=map(int,input().split())
dp=[0]*(10**5)
dps=[0]*(10**5)
for i in range(k-1):
    dp[i]=1
    dps[i]=i+1
dp[k-1]=2
dps[k-1]=dps[k-2]+2
l=k
for _ in range(t):
    a,b=map(int,input().split())
    if b>l:
        for z in range(l,b):
            dp[z]=(dp[z-1]+dp[z-k])%1000000007
            dps[z]=(dps[z-1]+dp[z])%1000000007
            l=b
    if a==1:
        print(dps[b-1])
    else:
        if dps[b-1]-dps[a-2]<0:
            print(dps[b-1]-dps[a-2]+1000000007)
        else:
            print(dps[b-1]-dps[a-2])