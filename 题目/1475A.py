n=int(input())
l=0
while True:
    if l==n:
        break
    k=int(input())
    while k%2==0:
        k=k/2
        continue
    if k==1:
        print('NO')
    else:
        print('YES')
    l+=1