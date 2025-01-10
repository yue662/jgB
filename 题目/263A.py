a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=list(map(int,input().split()))
i=0
k=0
while k<1:
    k=a[i]+b[i]+c[i]+d[i]+e[i]
    i=i+1
list=[a,b,c,d,e]
j=0
h=0
while h<1:
    h=sum(list[j])
    j=j+1
print(abs(i-3)+abs(j-3))
