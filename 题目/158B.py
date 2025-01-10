import math
n=int(input())
slist=list(map(int,input().split()))
a=0
b=0
c=0
d=0
k=0
for i in range(n):
    if slist[i]==1:
        a+=1
    elif slist[i]==2:
        b+=1
    elif slist[i]==3:
        c+=1
    else:
        d+=1
if a<=c:
    k=c+d+math.ceil(b/2)
elif a>c:
    k=d+c+math.ceil((a-c+2*b)/4)
print(k)