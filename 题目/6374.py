n=int(input())
st=str(input())
i=0
while True:
    if len(st)<81:
        print(st)
        break
    if ord(st[80-i])==32:
        print(st[:80-i])
        st=st[80-i+1:]
        i=0
    else:
        i+=1
    continue