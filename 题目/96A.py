st=str(input())
i=0
K=1
while True:
    if i==len(st)-1:
        print('NO')
        break
    if st[i]==st[i+1]:
        K+=1
        i+=1
    else:
        K=1
        i+=1
    if K==7:
        print('YES')
        break