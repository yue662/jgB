n=int(input())
adds=0
llist=list(map(int,input().split()))
for i in range(0,n):
    adds+=llist[i]
print(adds/n)