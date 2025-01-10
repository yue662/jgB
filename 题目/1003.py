while True:
    st=float(input())
    if st==0:
        break
    alls=0
    i=2
    while True:
        alls+=1/i
        if st<alls:
            print(str(i-1)+' card(s)')
            break
        i+=1
        continue