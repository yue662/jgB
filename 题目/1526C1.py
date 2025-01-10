n=int(input())
sl=list(map(int,input().split()))
mins=[]
alls=0
nl=n
for i in range(n):
    alls+=sl[i]
    if sl[i]<0:
        mins.append(sl[i])
        mins.sort()
        if alls<0:
            alls-=mins[0]
            nl-=1
            del mins[0]
print(nl)