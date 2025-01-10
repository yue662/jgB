n=int(input())
sl=[]
for _ in range(n):
    sl.append(list(map(int,input().split())))
nl=[]
while True:
    if n==0:
        break
    elif n==1:
        nl.append(sl[0][0])
        break
    z=0
    z+=sum(sl[0])+sum(sl[n-1])
    for i in range(1,n-1):
        z+=sl[i][0]+sl[i][n-1]
        del sl[i][0]
        del sl[i][n-2]
    del sl[0]
    del sl[n-2]
    nl.append(z)
    n-=2
    continue
print(max(nl))