m,n=map(int,input().split())
dx=[0,0,-1,1]
dy=[1,-1,0,0]
sl=[]
for _ in range(m):
    sl.append(list(map(int,input().split())))
outs=0
for i in range(m):
    for j in range(n):
        rt=0
        for p in range(4):
            if 0<=i+dx[p]<m and 0<=j+dy[p]<n:
                if sl[i+dx[p]][j+dy[p]]>sl[i][j]:
                    rt=1
                    break
        if rt==1:
            continue
        nl=[[(i,j)]]
        for k in range(n*m):
            nl.append([])
            if k!=0:
                nl[k-1]=0
            for l in range(len(nl[k])):
                x=nl[k][l][0]
                y=nl[k][l][1]
                for d in range(4):
                    nx=x+dx[d]
                    ny=y+dy[d]
                    if 0<=nx<m and 0<=ny<n:
                        if sl[nx][ny]<sl[x][y]:
                            nl[k+1].append((nx,ny))
            if len(nl[k+1])==0:
                outs=max(outs,k+1)
                break
print(outs)