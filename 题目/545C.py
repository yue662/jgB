n=int(input())
lx=[[int(x) for x in input().split()] for i in range(n)]
xlx=[lx[z+1][0]-lx[z][0] for z in range(n-1)]
s=2
for k in range(1,n-1):
    if lx[k][1]<xlx[k-1]:
        s+=1
    elif lx[k][1]<xlx[k]:
        s+=1
        xlx[k]=xlx[k]-lx[k][1]
if n==1:
    s=1
print(s)