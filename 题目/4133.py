d=int(input())
n=int(input())
sl=[]
for _ in range(n):
    sl.append(list(map(int,input().split())))
nl=[]
for i in range(0,1025):
    for j in range(0,1025):
        alls=0
        for k in range(len(sl)):
            if sl[k][0] in range(i-d,i+d+1) and sl[k][1] in range(j-d,j+d+1):
                alls+=sl[k][2]
        if alls>0:
            nl.append(alls)
print(nl.count(max(nl)),end=" ")
print(max(nl))