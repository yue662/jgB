k=int(input())
s=0
answer=[]
slist=[1,1]
for i in range(2,20):
    slist.append(slist[i-1]+slist[i-2])
while True:
    if s<k:
        n = int(input())
        answer.append(str(slist[n-1]))
        s=s+1
        continue
    if s==k:
        print('\n'.join(answer))
        break
