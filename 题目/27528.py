n=int(input())
dp=[1]*n
for i in range(1,n):
    for j in range(i):
        dp[i]+=dp[j]
print(dp[n-1])