n=int(input())
while True:
    if n%2==1:
        n=n*3+1
        print(str(int((n-1)/3))+"*3+1="+str(int(n)))
        if n==1:
            print("End")
            break
        else:
            continue
    if n%2==0:
        n=n/2
        print(str(int(2*n))+"/2="+str(int(n)))
        if n==1:
            print("End")
            break
        else:
            continue