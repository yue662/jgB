n=int(input())
sl=list(map(int,input().split()))
sl.sort()
nl=[]
z=0
for i in sl:
    if i!=z:
        nl.append([i,sl.count(i)])
        z=i
dp=[0]*len(nl)
dp[0]=nl[0][0]*nl[0][1]
if len(nl)>1:
    dp[1]=nl[1][0]*nl[1][1]
    for i in range(1,len(nl)):
        for j in range(i):
            if nl[j][0]<nl[i][0]-1:
                dp[i]=max(dp[i],dp[j]+nl[i][0]*nl[i][1])
print(max(dp))