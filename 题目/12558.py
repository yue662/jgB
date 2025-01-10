n,m=map(int,input().split())
k=0
sl=[]
for _ in range(n):
    sl.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if sl[i][j]==1:
            k+=4
            if i<n-1 and sl[i+1][j]==1:
                k-=2
            if j<m-1 and sl[i][j+1]==1:
                k-=2
print(k)