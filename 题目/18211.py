p=int(input())
nlist=list(map(int,input().split()))
nlist.sort()
s1=0
s2=0
while True:
    if len(nlist)==0:
        break
    if p>=nlist[0]:
        p-=nlist[0]
        del nlist[0]
        s1+=1
        continue
    elif s2<s1 and len(nlist)>1:
        p+=nlist[-1]
        del nlist[-1]
        s2+=1
        continue
    else:
        break
print(s1-s2)