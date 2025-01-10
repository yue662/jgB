import math
while True:
    n=int(input())
    if n!=0:
        i=0
        list_t=[]
        while i<n:
            a,b=map(int,input().split())
            t=4.5*3600/a+b
            if b>=0:
                list_t.append(t)
            i=i+1
            continue
        print(math.ceil(min(list_t)))
        continue
    else:
        break