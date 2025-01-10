n=int(input())
i=0
while True:
    if i==n:
        break
    slist=list(map(int,input().split()))
    slist.sort()
    if slist[0]+slist[1]==slist[2]:
        print("YES")
    else:
        print("NO")
    i+=1
    continue