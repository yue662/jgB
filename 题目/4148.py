i=1
while True:
    a,b,c,d=map(int,input().split())
    if a<0:
        break
    for z in range(d+1,d+21253):
        if (z-a)%23==0 and (z-b)%28==0 and (z-c)%33==0:
            tsi=z
    print('Case '+str(i)+': the next triple peak occurs in '+str(tsi-d)+' days.')
    i+=1
    continue