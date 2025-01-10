class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[]
        for _ in range(n):
            dp.append([0]*m)
        dp[0][0]=1
        for i in range(n):
            for j in range(m):
                if i-1>=0:
                    dp[i][j]+=dp[i-1][j]
                if j-1>=0:
                    dp[i][j]+=dp[i][j-1]
        return dp[n-1][m-1]