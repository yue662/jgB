n=int(input())
k=0
k+=n//100
n=n%100
k+=n//20
n=n%20
k+=n//10
n=n%10
k+=n//5
n=n%5
k+=n
print(k)