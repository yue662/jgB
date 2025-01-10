n=int(input())
sl=list(map(int,input().split()))
dp=[]
for _ in range(n):
    dp.append([0,0])
if sl[1]-sl[0]!=0:
    dp[1]=[2,sl[1]-sl[0]]
for i in range(2,n):
    for j in range(1,i):
        if dp[j][1]!=0:
            if (sl[i]-sl[j])/dp[j][1]<0:
                if dp[i][0]<dp[j][0]+1:
                    dp[i][1]=sl[i]-sl[j]
                    dp[i][0]=dp[j][0]+1
        else:
            if dp[i][0]<2 and sl[i]-sl[j]!=0:
                dp[i][1]=sl[i]-sl[j]
                dp[i][0]=2
dp.append([1,0])
dp.sort()
print(dp[n][0])