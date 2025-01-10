import math
t=int(input())
c=0
while c<t:
    a,b=map(int,input().split())
    i=b*math.ceil(a/b)-a
    print(i)
    c=c+1