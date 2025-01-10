n,k=map(int,input().split())
slist=list(map(int,input().split()))
outl=[]
sk=slist[k-1]
for i in range(0,n):
    if slist[i]>=sk and slist[i]>0:
        outl.append(1)
print(len(outl))