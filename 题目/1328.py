i=1
while True:
    if i>1:
        input()
    t=0
    n,d=map(int,input().split())
    if n==0:
        break
    xylist=[[int(x) for x in input().split()] for _ in range(n)]
    xylist.sort()
    for z in range(n):
        if xylist[z][1]>d:
            print('Case '+str(i)+': -1')
            t=1
            break
    if t==1:
        i+=1
        continue
    outs=1
    xs=xylist[0][0]+(d**2-xylist[0][1]**2)**(1/2)
    for k in range(1,n):
        if ((xylist[k][0]-xs)**2+xylist[k][1]**2)**(1/2)>d:
            if xylist[k][0]>xs:
                outs+=1
            xs=xylist[k][0]+(d**2-xylist[k][1]**2)**(1/2)
    print('Case '+str(i)+': '+str(outs))
    i+=1
    continue