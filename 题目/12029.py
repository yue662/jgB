k=int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for _ in range(k):
    m,n=map(int,input().split())
    sl=[]
    for i in range(m):
        sl.append(list(map(int,input().split())))
    I,J=map(int,input().split())
    p=int(input())
    out=0
    for j in range(p):
        if out==1:
            break
        x0,y0=map(int,input().split())
        h=sl[x0-1][y0-1]
        slist=[[[x0,y0]]]
        for l in range(m*n):
            if out==1:
                break
            if len(slist[l])==0:
                break
            slist.append([])
            for z in slist[l]:
                if out==1:
                    break
                for c in range(4):
                    nx=z[0]+dx[c]
                    ny=z[1]+dy[c]
                    if 0<nx<=m and 0<ny<=n and sl[nx-1][ny-1]<h and [nx,ny] not in slist[l+1]:
                        slist[l+1].append([nx,ny])
                        sl[nx-1][ny-1]=h
                        if nx==I and ny==J:
                            out=1
                            break
    if out==1:
        print("YES")
    else:
        print("NO")