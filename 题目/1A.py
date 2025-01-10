import math
n,m,a=map(int,input().split())
ns=math.ceil(n/a)
ms=math.ceil(m/a)
print(ns*ms)