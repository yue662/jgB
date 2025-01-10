dic={0:1,1:0}
while True:
    sl=list(map(int,input().split()))
    if sl[0]==0 and sl[1]==0:
        break
    s=0
    sl.sort()
    while True:
        if sl[1]/sl[0]>=2 or sl[1]==sl[0]:
            break
        else:
            sl[1]-=sl[0]
            sl.sort()
            s=dic[s]
            continue
    if s==0:
        print("win")
    else:
        print("lose")