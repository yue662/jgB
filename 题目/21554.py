n=int(input())
slist=list(map(int,input().split()))
ls=[(slist[i],i) for i in range(n)]
ls.sort()
for k in range(n):
    print(ls[k][1]+1,end=' ')
alltime=0
for i in range(n):
    alltime+=ls[i][0]*(n-1-i)
print('\n'+'{0:.2f}'.format(alltime/n))