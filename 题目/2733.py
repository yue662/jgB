a=int(input())
if a%4==0 and a%100!=0:
    print('Y')
elif a%400==0:
    print('Y')
else:
    print('N')