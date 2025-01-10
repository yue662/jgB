n,k,l,c,d,p,nl,np=map(int,input().split())
minn=min(k*l/nl/n,c*d/n,p/np/n)
print(int(minn//1))