slist=list(map(int,input().split()))
slist.sort()
outs=''
for i in range(3):
    outs+=str(slist[3]-slist[i])+' '
print(outs.rstrip())