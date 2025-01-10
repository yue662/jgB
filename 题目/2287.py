while True:
    n=int(input())
    if n==0:
        break
    sl1=list(map(int,input().split()))
    sl2=list(map(int,input().split()))
    sl1.append(0)
    sl1.sort()
    sl1.reverse()
    ql=1
    k=0
    z=0
    s=0
    p=0
    while True:
        if sl1[0]==0:
            break
        if sl1[0]<min(sl2):
            break
        for i in sl2:
            if i in range(sl1[1]+1,sl1[0]):
                k+=1
                sl2.remove(i)
            elif i==sl1[0]:
                p+=1
                sl2.remove(i)
        if k+p==0:
            ql-=1
            z+=1
        else:
            m=k+p
            if m-1<=z:
                ql+=2*(m-1)
                z=z-(m-1)
            elif m-1<=s+z:
                ql+=2*z+m-1-z
                z=0
                s=s-(m-1-z)
            else:
                ql+=2*z+s
                z=0
                s=0
            if k==0:
                s+=1
            else:
                ql+=1
        del sl1[0]
        k=0
        p=0
        continue
    ql-=len(sl1)
    print(200*ql)
    continue