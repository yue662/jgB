t=int(input())
i=0
while True:
    if i==t:
        break
    else:
        n = int(input())
        alist = list(map(int, input().split()))
        blist = list(map(int, input().split()))
        alla = sum(alist) + min(blist) * n
        allb = sum(blist) + min(alist) * n
        print(min(alla, allb))
        i+=1
        continue