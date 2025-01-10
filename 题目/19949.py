n=int(input())
sr=0
for i in range(n):
    st=str(input())
    l=0
    k=0
    j=0
    while True:
        if j>=len(st):
            break
        if ord(st[j])==35:
            if k%2==0:
                sr+=1
                if j==l and l!=0:
                    sr-=1
            k+=1
            l=j+4
            j+=3
        j+=1
        continue
print(sr)