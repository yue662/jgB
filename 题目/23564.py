st=int(input())
def sus(k):
    while True:
        k+=1
        j=0
        for i in range(2,k):
            if k%i==0:
                j+=1
                break
        if j==0:
            break
        else:
            continue
    return k
l=2
n=0
z=0
while True:
    if st%l==0:
        n+=1
        z+=1
        st=st/l
        continue
    elif z>1:
        break
    elif st==1:
        break
    else:
        l=sus(l)
        z=0
        continue
if z>1:
    print(0)
elif n%2==0:
    print(1)
else:
    print(-1)