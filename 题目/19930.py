n,m=map(int,input().split())
sl=[]
z=0
for _ in range(n):
    sl.append(list(map(int,input().split())))
if sl[0][0]==1:
    print(0)
elif sl[0][0]==2:
    print('NO')
else:
    zl=[[(0,0)]]
    sl[0][0]=3
    for i in range(n*m):
        zl.append([])
        for j in range(len(zl[i])):
            for k in (zl[i][j][0]+1,zl[i][j][0]-1):
                if k<0 or k>=n:
                    continue
                if sl[k][zl[i][j][1]]==0:
                    zl[i+1].append((k,zl[i][j][1]))
                    sl[k][zl[i][j][1]]=3
                if sl[k][zl[i][j][1]]==1:
                    z=1
                    print(i+1)
                    break
            if z==1:
                break
            for l in (zl[i][j][1]+1,zl[i][j][1]-1):
                if l<0 or l>=m:
                    continue
                if sl[zl[i][j][0]][l]==0:
                    zl[i+1].append((zl[i][j][0],l))
                    sl[zl[i][j][0]][l]=3
                if sl[zl[i][j][0]][l]==1:
                    z=1
                    print(i+1)
                    break
        if z==1:
            break
        if len(zl[i+1])==0:
            break
    if z==0:
        print('NO')