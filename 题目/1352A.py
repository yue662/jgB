t=int(input())
z=0
while True:
    if z==t:
        break
    n=str(input())
    k=0
    outs=''
    for i in range(0,len(n)):
        if n[i]!='0':
            k+=1
            outs+=n[i]+'0'*(len(n)-i-1)+' '
    print(k)
    print(outs.rstrip())
    z+=1
    continue