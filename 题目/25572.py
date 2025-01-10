n=int(input())
sl=[]
for i in range(n):
    sl.append(list(map(int,input().split())))
bl=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for i in range(n):
    for j in range(n):
        if sl[i][j]==5:
            bl.append([i,j])
def dfs1(x,y,visited):
    global z
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n-1 and visited[nx][ny]==0 and sl[nx][ny]!=1 and sl[nx][ny+1]!=1:
            if sl[nx][ny]==9 or sl[nx][ny+1]==9:
                z=1
                return
            visited[nx][ny]=1
            dfs1(nx,ny,visited)
            visited[nx][ny]=0
def dfs2(x,y,visited):
    global z
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n-1 and 0<=ny<n and visited[nx][ny]==0 and sl[nx][ny]!=1 and sl[nx+1][ny]!=1:
            if sl[nx][ny]==9 or sl[nx+1][ny]==9:
                z=1
                return
            visited[nx][ny]=1
            dfs2(nx,ny,visited)
            visited[nx][ny]=0
visited=[[0]*n for j in range(n)]
visited[bl[0][0]][bl[0][1]]=1
if bl[0][0]==bl[1][0]:
    z=0
    dfs1(bl[0][0],bl[0][1],visited)
    if z==1:
        print("yes")
    else:
        print("no")
elif bl[0][1]==bl[1][1]:
    z=0
    dfs2(bl[0][0],bl[0][1],visited)
    if z==1:
        print("yes")
    else:
        print("no")