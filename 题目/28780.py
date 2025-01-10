import math
n,m=map(int,input().split())
ll=list(map(int,input().split()))
ll.sort()
dp=[0]
for _ in range(m):
    dp.append(math.inf)
for i in range(1,m+1):
    for z in range(n):
        if ll[z]<=i:
            dp[i]=min(dp[i],dp[i-ll[z]]+1)
if dp[m]!=math.inf:
    print(dp[m])
else:
    print(-1)