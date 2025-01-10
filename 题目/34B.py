n,m=map(int,input().split())
slist=list(map(int,input().split()))
alls=0
i=0
while True:
    if i==m:
        break
    a=min(slist)
    slist.remove(a)
    if a<0:
        i+=1
        alls-=a
        continue
    else:
        break
print(alls)