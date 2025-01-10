n=int(input())
for _ in range(n):
    st=int(input())
    i=0
    while True:
        if st%3==0:
            st=st/3
            i+=1
            continue
        else:
            break
    j=0
    while True:
        if st%2==0:
            st=st/2
            j+=1
            continue
        else:
            break
    if st==1:
        if i>=j:
            print(2*i-j)
        else:
            print(-1)
    else:
        print(-1)
