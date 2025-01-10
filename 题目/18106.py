import math
n=int(input())
sl=[]
for _ in range(n):
    sl.append([0]*n)
l0=1
for k in range(math.ceil(n//2)):
    for i in range(n-2*k):
        sl[k][i+k]=i+l0
    for j in range(n-2*k-1):
        sl[k+j+1][n-1-k]=j+l0+n-2*k
    for l in range(n-2*k-1):
        sl[n-1-k][n-2-l-k]=l+l0+2*(n-2*k-1)+1
    for m in range(n-2*k-2):
        sl[n-m-k-2][k]=m+l0+3*(n-2*k-1)+1
    l0+=4*(n-2*k-1)
if n%2==1:
    sl[n//2][n//2]=n**2
for i in range(n):
    for j in range(n):
        print(sl[i][j],end=' ')
    print()