n=int(input())
slist=list(map(str,input()))
dics={'R':1,'G':2,'B':3}
k=0
for i in range(n-1):
    if dics[slist[i]]==dics[slist[i+1]]:
        k=k+1
print(k)