n,a,b,c=map(int,input().split())
sl=[]
for i in range(n//a+1):
    for j in range((n-i*a)//b+1):
        if (n-i*a-j*b)%c==0:
            sl.append(i+j+(n-i*a-j*b)//c)
print(max(sl))