t=1
while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    sl=[]
    for _ in range(w):
        sl.append(str(input()))
        print('Board #'+str(t)+':')
        t+=1
    n=1
    while True:
        x1,y1,x2,y2=map(int,input().split())
        if x1==0 and y1==0 and x2==0 and y2==0:
            break
        print('Pair '+str(n)+': '++'.')
        continue
    print('\n')
    continue