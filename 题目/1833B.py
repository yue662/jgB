t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    ilist=list(map(int,input().split()))
    slist=list(map(int,input().split()))
    olist = [(ilist[i], i) for i in range(n)]
    olist.sort()
    slist.sort()
    outs = ''
    for k in range(n):
        ilist[olist[k][1]] = slist[k]
    for z in range(n):
        print(ilist[z], end=' ')
    print()