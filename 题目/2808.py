L,M=map(int,input().split())
ll=set(range(0,L+1))
i=0
while i<M:
    a,b=map(int,input().split())
    for k in range(a,b+1):
        ll.discard(k)
    i=i+1
print(len(ll))