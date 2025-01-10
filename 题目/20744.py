import math
sl=list(map(int,input().split(',')))
nl=[0]
for e in range(len(sl)):
    nl.append(nl[e]+sl[e])
dp=[[sl[0]]]
for k in range(1,len(sl)):
    dp.append([math.inf]*k)
for i in range(1,len(sl)):
    dp[i].append(sl[i])
    for j in range(1,i+1):
        dp[i][i-j]=min(dp[i][i-j+1],sl[i-j])
    del dp[i][i]
out=max(sl)
for m in range(1,len(sl)+1):
    for n in range(m-1):
        s=dp[m-1][n]
        if s<0:
            out=max(out,nl[m]-nl[n]-s)
        else:
            out=max(out,nl[m]-nl[n])
print(out)