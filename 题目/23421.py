n,b=map(int,input().split())
slist=list(map(int,input().split()))
nlist=list(map(int,input().split()))
dp=[0]*(b+1)
hl=[]
for _ in range(b+1):
    hl.append([])
for i in range(b+1):
    zl=[]
    for j in range(n):
        if nlist[j]<=i and dp[i-nlist[j]]+slist[j]>dp[i] and j not in hl[i-nlist[j]]:
            dp[i]=dp[i-nlist[j]]+slist[j]
            zl.append(j)
    if len(zl)>0:
        hl[i]+=hl[i-nlist[max(zl)]]
        hl[i].append(max(zl))
print(max(dp))