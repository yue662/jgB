n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    l=0
    for k1 in (1,-1):
        for k2 in (1,-1):
            for k3 in (1,-1):
                for k4 in (1,-1):
                    if a*k1+b*k2+c*k3+d*k4==24:
                        print("YES")
                        l=1
                        break
                if l==1:
                    break
            if l==1:
                break
        if l==1:
            break
    if l==0:
        print("NO")