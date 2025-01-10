slist=list(map(str,input()))
setl=set()
for i in range(0,len(slist)):
    setl.add(slist[i])
if len(setl)%2==0:
    print("CHAT WITH HER")
else:
    print("IGNORE HIM!")