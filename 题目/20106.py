import math
n,m,p=map(int,input().split())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
sl=[]
out=''
for _ in range(n):
    sl.append(list(map(str,input().split())))
def dfs(x,y,check,s):
    global mins
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if check[nx][ny]==0 and ord(sl[nx][ny])!=35:
                check[nx][ny]=1
                z=abs(int(sl[x][y])-int(sl[nx][ny]))
                s+=z
                if s<mins:
                    if nx==x2 and ny==y2:
                        mins=s
                    else:
                        dfs(nx,ny,check,s)
                check[nx][ny]=0
                s-=z
for _ in range(p):
    x1,y1,x2,y2=map(int,input().split())
    if ord(sl[x1][y1])==35 or ord(sl[x2][y2])==35:
        print('NO')
        continue
    check=[[0]*m for k in range(n)]
    s=0
    mins=math.inf
    dfs(x1,y1,check,s)
    if mins==math.inf:
        out=out+'NO'+'\n'
    else:
        out=out+str(mins)+'\n'
print(out)