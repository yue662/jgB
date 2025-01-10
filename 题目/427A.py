n=int(input())
shi=list(map(int,input().split()))
i=0
k=0
add=0
while i<n:
    add=add+shi[i]
    if add<0:
        add=0
        k=k+1
    i=i+1
print(k)