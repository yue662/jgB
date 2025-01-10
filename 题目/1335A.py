import math
t=int(input())
i=0
while True:
    if i==t:
        break
    n=int(input())
    print(math.ceil(n/2)-1)
    i+=1
    continue