n,m=map(int,input().split())
if n%(m-1)!=0:
    print(n//(m-1)*m+n%(m-1))
else:
    print(n//(m-1)*m-1)