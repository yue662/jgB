sl=[]
nl=[20001]
while True:
    try:
        a=str(input())
        if 'pop' in a:
            if len(sl)!=0:
                if sl[-1] in nl and sl[-1] not in sl[:-2]:
                    nl.remove(sl[-1])
                del sl[-1]
        elif 'min' in a:
            if len(sl)!=0:
                print(nl[-1])
        elif 'push' in a:
            z=int(a[5:])
            sl.append(z)
            if z<nl[-1]:
                nl.append(z)
        continue
    except EOFError:
        break