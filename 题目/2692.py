n=int(input())
dic={'up 0':'heavy. ','up 1':'light. ','down 0':'light. ','down 1':'heavy. ','up0':'heavy. ','up1':'light. ','down0':'light. ','down1':'heavy. '}
for _ in range(n):
    sl=[]
    for o in range(3):
        sl.append(str(input()))
    lists=['A','B','C','D','E','F','G','H','I','J','K','L']
    for i in range(3):
        if 'even' in sl[i]:
            for j in range(9):
                if sl[i][j] in lists:
                    lists.remove(sl[i][j])
        else:
            lists1=lists[:]
            for k in lists1:
                if k not in sl[i][:9]:
                    lists.remove(k)
    for n in range(len(lists)):
        s=lists[n]
        nl=[]
        for m in range(3):
            if s in sl[m]:
                if s in sl[m][:4]:
                    t=sl[m][10:]+'0'
                else:
                    t=sl[m][10:]+'1'
                nl.append(dic[t])
        if nl.count(nl[0])!=len(nl):
            continue
        else:
            break
    print(s+' is the counterfeit coin and it is '+nl[0])