n,m=map(int,input().split())
sl=[]
for _ in range(n):
    sl.append(list(map(int,input().split())))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
outs=[]
def dfs(st,x,y,nl):
    global outs
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and (nx,ny) not in nl:
            nl.append((nx,ny))
            st+=sl[nx][ny]
            if nx==n-1 and ny==m-1:
                outs.append([st,nl])
            else:
                dfs(st,nx,ny,nl[:])
            del nl[-1]
            st-=sl[nx][ny]
dfs(sl[0][0],0,0,[(0,0)])
outs.sort()
for i in outs[-1][1]:
    print(i[0]+1,i[1]+1)
print(n,m)