n=int(input())
i=0
xil=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
dic={'1':0,'0':1,'X':2,'9':3,'8':4,'7':5,'6':6,'5':7,'4':8,'3':9,'2':10}
while i<n:
    sfz=str(input())
    lsfz=[]
    for k in range(0,18):
        lsfz.append(sfz[k])
        addstu=0
    for z in range(0,17):
        addstu+=int(lsfz[z])*xil[z]
    endstu=addstu%11
    if endstu==dic[lsfz[17]]:
        print("YES")
        i=i+1
        if i==n:
            break
        else:
            continue
    else:
        print("NO")
        i=i+1
        if i==n:
            break
        else:
            continue