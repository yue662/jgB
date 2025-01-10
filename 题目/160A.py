n=int(input())
slist=list(map(int,input().split()))
i=0
adds=0
while True:
    a=max(slist)
    slist.remove(a)
    adds+=a
    i+=1
    if adds>sum(slist):
        break
    else:
        continue
print(i)