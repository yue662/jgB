a=0
n=int(input())
for i in range(1,n+1):
    if i%7!=0 and i%10!=7 and i//10!=7:
        a=a+i*i
print(a)