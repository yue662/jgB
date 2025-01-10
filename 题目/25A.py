n=int(input())
slist=list(map(int,input().split()))
rdict={}
sall=0
for i in range(n):
    rdict[slist[i]%2]=(i+1)
    sall+=slist[i]%2
if sall/n>0.5:
    print(rdict[0])
else:
    print(rdict[1])