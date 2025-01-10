t=int(input())
ol=[]
for _ in range(t):
    n,m=map(int,input().split())
    sl=[]
    for i in range(n):
        sl.append(str(input()))
    zl=[]
    for k in range(n):
        for l in range(m):
            if ord(sl[k][l])==87:
                zl.append((k,l))
    out=[0]
    while True:
        if len(zl)==0:
            break
        il=[zl[0]]
        del zl[0]
        for d in range(n*m):
            for si in zl:
                if si[0] in (il[d][0]-1,il[d][0],il[d][0]+1) and si[1] in (il[d][1]-1,il[d][1],il[d][1]+1):
                        il.append(si)
            for j in il:
                if j in zl:
                    zl.remove(j)
            if d==len(il)-1:
                break
        out.append(len(il))
        continue
    ol.append(max(out))
for a in ol:
    print(a)