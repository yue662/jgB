import math
n=int(input())
nl=[]
for i in range(n):
    t=str(input())
    nl.append([])
    for j in range(n):
        nl[i].append([math.inf,int(t[j]),0])
def di(sl):
    global z
    z=0
    s=math.inf
    for m in range(n):
        for c in range(n):
            if sl[m][c][0]<s and sl[m][c][2]==0:
                s=sl[m][c][0]
                x=m
                y=c
    sl[x][y][2]=1
    for o in range(4):
        nx=x+dx[o]
        ny=y+dy[o]
        if 0<=nx<n and 0<=ny<n and sl[nx][ny][2]==0:
            t=sl[x][y][1]
            p=sl[nx][ny][1]
            if t==0 and p==1:
                z=1
                break
            else:
                sl[nx][ny][0]=min(sl[x][y][0]+dic[(t,p)],sl[nx][ny][0])
    if z==1:
        print(sl[x][y][0])
    else:
        di(sl)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
dic={(1,1):0,(1,0):1,(0,0):1}
e=0
for k in range(n):
    for l in range(n):
        if nl[k][l][1]==1:
            nl[k][l][0]=0
            e=1
            break
    if e==1:
        break
di(nl)