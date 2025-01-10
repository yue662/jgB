import math
l,n,m=map(int,input().split())
sl=[]
a,b=0,0
for i in range(n):
    a=b
    b=int(input())
    sl.append(b-a)
sl.append(l-b)
def f(z,nl):
    if z==0:
        print(min(nl))
        exit()
    else:
        k=math.inf
        for i in range(len(nl)):
            if nl[i]<k:
                k=nl[i]
                s=i
        if s==0:
            nl[0]+=nl[1]
            del nl[1]
        elif s==len(nl)-1:
            nl[-1]+=nl[-2]
            del nl[-2]
        elif nl[s+1]<nl[s-1]:
            nl[s]+=nl[s+1]
            del nl[s+1]
        else:
            nl[s]+=nl[s-1]
            del nl[s-1]
        f(z-1,nl)
f(m,sl)