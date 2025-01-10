n=str(input())
z=0
sl=[[0]]
for i in range(len(n)+1):
    sl.append([])
    for j in range(len(sl[i])):
        for k in range(sl[i][j],len(n)):
            if (int(n[sl[i][j]:k+1])**(1/2))%1==0 and int(n[sl[i][j]:k+1])!=0:
                if k==len(n)-1:
                    z=1
                    break
                else:
                    sl[i+1].append(k+1)
        if z==1:
            break
    if z==1:
        break
    if len(sl[i+1])==0:
        break
if z==1:
    print("Yes")
else:
    print("No")