n=int(input())
slist=[['1'],['1 2 ','2 1 ']]
for _ in range(n-1):
    slist.append([])
k=2
while True:
    if n==1:
        break
    if k==n:
        break
    for i in range(len(slist[k-1])):
        for j in range(1,k):
            slist[k].append(slist[k-1][i][0:2*j]+str(k+1)+' '+slist[k-1][i][2*j:])
        slist[k].append(str(k+1)+' '+slist[k-1][i])
        slist[k].append(slist[k-1][i]+str(k+1)+' ')
    k+=1
slist[n-1].sort()
for z in range(len(slist[n-1])):
    print(slist[n-1][z].strip())