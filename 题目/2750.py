x=0
y=0
a=int(input())
if a%2!=0:
    x=y=0
else:
    y=a//2
if y%2!=0:
    x=y//2+1
else:
    x=y//2
print(x,y)