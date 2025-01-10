str1=input().lower()
str2=input().lower()
i=0
while i<len(str1):
    if ord(str1[i])<ord(str2[i]):
        print(-1)
        break
    elif ord(str1[i])>ord(str2[i]):
        print(1)
        break
    else:
        i=i+1
        continue
if i==len(str1):
    print(0)
