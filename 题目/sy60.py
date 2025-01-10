a,b=map(int,input().split())
i=0
li=[]
for sy in range(a,b+1):
    sy1=int(str(sy)[0])
    sy2=int(str(sy)[1])
    sy3=int(str(sy)[2])
    if sy1**3+sy2**3+sy3**3==sy:
        li.append(str(sy))
        i=i+1
if i==0:
    print('NO')
else:
    pr = li[0] + ' '
    for k in range(1, len(li)):
        pr = pr + li[k] + ' '
    print(pr.rstrip())