n=int(input())
slist=list(map(int,input().split()))
i=0
while True:
    if i==n:
        break
    z=1
    for k in range(1,slist[i]//2+1):
        if slist[i]%k==0:
            z+=1
            if z>3:
                break
    if z==3:
        print('YES')
    else:
        print('NO')
    i+=1
    continue