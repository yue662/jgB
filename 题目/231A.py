m=0
t=0
n=int(input())
while t<n:
    a,b,c=map(int,input().split())
    t=t+1
    if a+b+c>=2:
        m=m+1
print(m)