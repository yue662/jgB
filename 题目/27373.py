import decimal
m=int(input())
n=int(input())
nl=list(map(str,input().split()))
for i in range(n):
    nl[i]=[decimal.Decimal('0.'+(nl[i]*((20//len(nl[i]))+1))),nl[i],len(nl[i])]
nl.sort(reverse=True)
def dfs(out,k,check):
    global z
    s=0
    for a in range(n):
        if check[a]==0:
            if k+nl[a][2]==m:
                s=1
                z=1
                print(str(out+nl[a][1]))
                exit()
            elif k+nl[a][2]<m:
                s=1
                check[a]=1
                k+=nl[a][2]
                out=out+nl[a][1]
                dfs(out,k,check)
                check[a]=0
                k-=nl[a][2]
                out=out[:k]
    if s==0:
        dp.append(out)
z=0
check=[0]*n
dp=[]
dfs('',0,check)
if z==0:
    print(max(dp))